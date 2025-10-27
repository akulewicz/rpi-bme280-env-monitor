from fastapi import FastAPI
from .services.bme280_service import read_bme280_data

app = FastAPI()


@app.get("/env")
async def root():
    data = read_bme280_data()
    return {"rpi": data}