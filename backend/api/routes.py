from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.ocr_service import OCRService

router = APIRouter(prefix="/api/v1/ocr", tags=["OCR"])
ocr_service = OCRService()

@router.post("/front")
async def ocr_front(image: UploadFile = File(...)):
    if not image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    contents = await image.read()
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")
        
    result = ocr_service.process_front(contents)
    return result

@router.post("/back")
async def ocr_back(image: UploadFile = File(...)):
    contents = await image.read()
    result = ocr_service.process_back(contents)
    return result

@router.post("/full")
async def ocr_full(front_image: UploadFile = File(...), back_image: UploadFile = File(...)):
    front_contents = await front_image.read()
    back_contents = await back_image.read()
    
    front_res = ocr_service.process_front(front_contents)
    back_res = ocr_service.process_back(back_contents)
    
    return {
        "success": front_res.success and back_res.success,
        "front": front_res,
        "back": back_res
    }
