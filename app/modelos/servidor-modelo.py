from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import ulid
from ..database import Base

class Servidor(Base):
    """
    Modelo de servidores on-premise
    """
    __tablename__ = "servidores"

    id = Column(Integer, primary_key=True, index=True)
    ulid = Column(String, unique=True, index=True, nullable=False)
    nome = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    ultimo_dado_em = Column(DateTime(timezone=True), nullable=True)

    usuario = relationship("Usuario")
    dados = relationship("DadoSensor", back_populates="servidor")

    def gerar_ulid(self):
        """
        Gera um ULID único para o servidor
        """
        return str(ulid.new())
