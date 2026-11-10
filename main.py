from fastapi import FastAPI, UploadFile, File

app = FastAPI(title="AI Skincare Analyzer")

@app.get("/")
def home():
    return {"message": "AI Skincare Analzyer API is running"}

@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    return{
        "filename": image.filename,
        "content_type": image.content_type,
        "status": "image recieved"
    }