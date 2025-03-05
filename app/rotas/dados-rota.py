from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from typing import List, Optional

from ..database import obter_sessao_bd
from ..modelos.dados_sensor import DadoSensor
from ..modelos.servidor import Servidor
from ..esquemas.dados_sensor import DadoSensorCriacao, DadoSensorResposta
from ..servicos.autenticacao import obter_usuario_atual
from ..modelos.usuario import Usuario

roteador = APIRouter()

@roteador.post("/", status_code=status.HTTP_201_CREATED)
def registrar_dado_sensor(
    dado: DadoSensorCriacao,
    sessao: Session = Depends(obter_sessao_bd)
):
    """
    Endpoint para registrar dados de sensores
    """
    # Verificar se o servidor existe
    servidor = sessao.query(Servidor).filter(Servidor.ulid == dado.server_ulid).first()
    
    if not servidor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Servidor não encontrado"
        )
    
    # Validar se pelo menos um sensor foi enviado
    if not any([
        dado.temperature, 
        dado.humidity, 
        dado.voltage, 
        dado.current
    ]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pelo menos um dado de sensor deve ser enviado"
        )
    
    # Criar registro de dados do sensor
    novo_dado = DadoSensor(
        servidor_ulid=dado.server_ulid,
        timestamp=dado.timestamp,
        temperatura=dado.temperature,
        umidade=dado.humidity,
        tensao=dado.voltage,
        corrente=dado.current
    )
    
    # Atualizar último dado do servidor
    servidor.ultimo_dado_em = dado.timestamp
    
    sessao.add(novo_dado)
    sessao.commit()
    
    return {"mensagem": "Dados do sensor registrados com sucesso"}

@roteador.get("/", response_model=List[DadoSensorResposta])
def consultar_dados_sensor(
    server_ulid: Optional[str] = None,
    start_time: Optional[datetime] = None,