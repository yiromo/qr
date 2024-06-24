import qrcode
import json
import segno
from fastapi.responses import FileResponse
from fastapi import HTTPException

def generate_qr_code(data: str) -> str:
    try:
        qrcode = segno.make_qr(data)
        file_path = "qr.png"
        qrcode.save(file_path, scale=10, border=0)
        return file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def generate_qr_img(json_data: dict) -> str:
    try:
        json_str = json.dumps(json_data)
        return generate_qr_code(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))