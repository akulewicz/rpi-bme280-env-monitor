from pydantic import BaseModel
from typing import Optional

class EnvData(BaseModel):
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None