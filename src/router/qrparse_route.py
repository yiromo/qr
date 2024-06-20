from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from schemas.schema01 import parse_qr_code

router = APIRouter(
    prefix="/QRparse",
    tags=["QR PARSE"]
)

@router.post("/parse_qr/")
async def parse_qr(file: UploadFile = File(...)):
    return await parse_qr_code(file)