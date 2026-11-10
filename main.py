from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Skincare Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 10 * 1024 * 1024 #10mb

@app.get("/")
def home():
    return {"message": "AI Skincare Analzyer API is running"}

@app.post("/analyze")
async def analyze_image(
    image: UploadFile = File(...),
    goal: str = Form(...),
    sensitive_skin: bool = Form(...),
    budget: str = Form(...)
    ):

    #checking if image
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an image file."
        )

    image_data = await image.read()

    #checking if exceeds 10mb
    if len(image_data) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Image cannot exceed 10mb"
        )

    return{
        "filename": image.filename,
        "content_type": image.content_type,
        "size_bytes": len(image_data),
        "preferences": {
            "goal": goal,
            "sensitive_skin": sensitive_skin,
            "budget": budget
        },
        "status": "image validated successfully"
    }