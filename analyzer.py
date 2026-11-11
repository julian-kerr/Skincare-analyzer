def analyze_skin_image(image_data: bytes) -> dict:
    """
    Temporary prototype analyzer.

    The function accepts the uploaded image bytes and returns
    the same structured format a real computer-vision model would return.
    """

    return {
        "detected_concerns": [
            {
                "name": "redness",
                "confidence": 0.78
            },
            {
                "name": "blemishes",
                "confidence": 0.64
            }
        ],
        "analysis_type": "mock"
    }