import base64
import json

from ollama import chat


MODEL_NAME = "qwen2.5vl:3b"


def analyze_skin_image(image_data: bytes) -> dict:
    encoded_image = base64.b64encode(image_data).decode("utf-8")

    prompt = """
Analyze this image for cosmetic skincare concerns only.

Do not diagnose diseases or make medical claims.

Choose only from these concern names:
- redness
- blemishes
- dryness
- oiliness
- dark_spots
- texture

Return ONLY valid JSON in this exact format:

{
  "detected_concerns": [
    {
      "name": "redness",
      "confidence": 0.0,
      "evidence": "short visual explanation"
    }
  ],
  "image_quality": {
    "usable": true,
    "reason": "short explanation"
  },
  "analysis_type": "local_vision_model"
}

Confidence must be a number between 0.0 and 1.0.

Return an estimated confidence score for display only.
This is not a medically calibrated probability.

Do not default to 0.80. Choose the confidence based on the visual strength of the evidence:
- 0.90–1.00: very clear
- 0.70–0.89: reasonably clear
- 0.50–0.69: uncertain
- below 0.50: weak evidence

If the image is unclear or not a usable skin photo, return an empty concerns list and set usable to false.
"""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [encoded_image],
            }
        ],
        options={
            "num_ctx": 8192,
            "temperature": 0.0,
            "seed": 42,
        },
    )

    raw_content = response["message"]["content"]
    result = json.loads(raw_content)

    return result