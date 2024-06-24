from fastapi import FastAPI
from qr_decode.qrparse_route import router as qrdecode
from qr_gen.qrgen_route import router as qrgen
from uuid_gen.uuid_route import router as uuidgen
app = FastAPI()

app.include_router(qrdecode)
app.include_router(qrgen)
app.include_router(uuidgen)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)