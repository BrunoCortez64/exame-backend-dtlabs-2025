from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database import Base
import ulid

class Usuario(Base):
    """
    Modelo de usuário para autenticação
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    
    def gerar_ulid(self):
        """
        Gera um ULID único para o usuário
        """
        return str(ulid.new())
