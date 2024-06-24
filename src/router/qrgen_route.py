from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from schemas.schema02 import generate_qr_img, generate_qr_code

router = APIRouter(
    prefix="/QRgen",
    tags=["QR Generator"]
)

@router.post("/generate_qr_code/")
async def generate_qr(data: str):
    file_path = generate_qr_code(data)
    return FileResponse(file_path, media_type='image/png', filename="qr.png")

@router.post("/generate_qr_with_json_data/")
async def generate_qr_with_json(json_data: dict):
    file_path = await generate_qr_img(json_data)
    return FileResponse(file_path, media_type='image/png', filename="qr.png")
