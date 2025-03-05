from sqlalchemy import Column, Float, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class DadoSensor(Base):
    """
    Modelo para armazenar dados de sensores
    """
    __tablename__ = "dados_sensores"

    id = Column(Integer, primary_key=True, index=True)
    servidor_ulid = Column(String, ForeignKey('servidores.ulid'), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    temperatura = Column(Float, nullable=True)
    umidade = Column(Float, nullable=True)
    tensao = Column(Float, nullable=True)
    corrente = Column(Float, nullable=True)

    servidor = relationship("Servidor", back_populates="dados")
