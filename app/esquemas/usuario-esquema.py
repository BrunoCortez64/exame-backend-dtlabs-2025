from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    usuario: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UsuarioCriacao(UsuarioBase):
    senha: str = Field(..., min_length=6)

class UsuarioResposta(UsuarioBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True

class TokenResposta(BaseModel):
    access_token: str
    token_type: str

class DadosToken(BaseModel):
    sub: Optional[str] = None
