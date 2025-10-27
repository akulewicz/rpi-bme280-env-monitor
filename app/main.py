from fastapi import FastAPI
from .services.bme280_service import read_bme280_data
from .schemas.env_data import EnvData

app = FastAPI()


@app.get("/env", response_model=EnvData)
async def root():
    return read_bme280_data()