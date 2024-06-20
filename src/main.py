from fastapi import FastAPI
from router.qrparse_route import router as qrdecode
from router.qrgen_route import router as qrgen
app = FastAPI()

app.include_router(qrdecode)
app.include_router(qrgen)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)