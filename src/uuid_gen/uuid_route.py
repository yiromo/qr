from fastapi import APIRouter, Query
import uuid

router = APIRouter(
    prefix="/UUID_Gen",
    tags=["UUID GEN"]
)

@router.get("/generate_uuid/")
async def generated_uuid(
    hyphens: bool = Query(True, description="Include hyphens in UUID"),
    braces: bool = Query(False, description="Include braces in UUID"),
    uppercase: bool = Query(False, description="Use uppercase letters in UUID"),
    quotes: bool = Query(False, description="Include quotes around UUID"),
    commas: bool = Query(False, description="Include commas in UUID")
):
    generated_uuid = str(uuid.uuid4())
    
    if not hyphens:
        generated_uuid = generated_uuid.replace('-', '')
    
    if braces:
        generated_uuid = '{' + generated_uuid + '}'
    
    if uppercase:
        generated_uuid = generated_uuid.upper()
    
    if quotes:
        generated_uuid = '"' + generated_uuid + '"'
    
    if commas:
        generated_uuid = ', '.join(generated_uuid[i:i+1] for i in range(len(generated_uuid)))
    
    return generated_uuid