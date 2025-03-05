from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DadoSensorCriacao(BaseModel):
    server_ulid: str
    timestamp: datetime
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    voltage: Optional[float] = None
    current: Optional[float] = None

    class Config:
        json_schema_extra = {
            "example": {
                "server_ulid": "01JMG0J6BH9JV08PKJD5GSRM84",
                "timestamp": "2024-02-19T12:34:56Z",
                "temperature": 25.5,
                "humidity": 60.2
            }
        }

class DadoSensorResposta(BaseModel):
    timestamp: datetime
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    voltage: Optional[float] = None
    current: Optional[float] = None
