import logging
from pyzbar.pyzbar import decode
from fastapi import UploadFile, HTTPException
from PIL import Image
import io
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def decode_qr_code(image):
    try:
        return decode(image)
    except Exception as e:
        logger.error(f"Error decoding QR code with pyzbar: {e}", exc_info=True)
        return []
    
async def parse_qr_code(file: UploadFile):
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        logger.info("Image successfully opened")

        decoded_objects = decode_qr_code(image)
        logger.info(f"Decoded objects: {decoded_objects}")

        if decoded_objects:
            qr_data_list = []
            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                logger.info(f"Decoded data: {data}")
                try:
                    json_data = json.loads(data)
                    qr_data_list.append(json_data)
                except json.JSONDecodeError:
                    qr_data_list.append(data)
            
            return {"qr_data": qr_data_list}
        else:
            return decoded_objects
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error parsing QR code: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An error occurred while processing the QR code.")
