from fastapi import FastAPI
from .services.bme280_service import read_bme280_data
from .schemas.env_data import EnvData
import logging

app = FastAPI()

logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="{asctime} [{levelname}] {name}: {message}",
                    style="{")

logging.getLogger("watchfiles").setLevel(logging.WARNING)
logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


@app.get("/env", response_model=EnvData)
async def root():
    return read_bme280_data()