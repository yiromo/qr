from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from schemas.schema01 import parse_qr_code

router = APIRouter(
    prefix="/QR_Decode",
    tags=["QR Decode"]
)

@router.post("/decode_qr/")
async def decode_qr(file: UploadFile = File(...)):
    return await parse_qr_code(file)