from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from schemas.schema01 import generate_qr_img

router = APIRouter(
    prefix="/QRgen",
    tags=["QR Generator"]
)

@router.post("/generate_qr/")
async def generate_qr(json_data: dict):
    pass