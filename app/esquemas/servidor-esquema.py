from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ServidorCriacao(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)

class ServidorResposta(BaseModel):
    ulid: str
    nome: str
    criado_em: datetime
    status: Optional[str] = None

class StatusSaude(BaseModel):
    server_ulid: str
    status: str
    server_name: str
