from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import obter_sessao_bd
from ..modelos.servidor import Servidor
from ..esquemas.servidor import ServidorCriacao, ServidorResposta
from ..servicos.autenticacao import obter_usuario_atual
from ..modelos.usuario import Usuario

roteador = APIRouter()

@roteador.post("/", response_model=ServidorResposta)
def criar_servidor(
    servidor: ServidorCriacao,
    usuario_atual: Usuario = Depends(obter_usuario_atual),
    sessao: Session = Depends(obter_sessao_bd)
):
    """
    Endpoint para criar um novo servidor
    """
    # Gerar ULID único para o servidor
    novo_servidor = Servidor(
        nome=servidor.nome,
        ulid=Servidor().gerar_ulid(),
        usuario_id=usuario_atual.id
    )
    
    sessao.add(novo_servidor)
    sessao.commit()
    sessao.refresh(novo_servidor)
    
    return novo_servidor
