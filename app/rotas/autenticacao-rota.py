from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import obter_sessao_bd
from ..modelos.usuario import Usuario
from ..esquemas.usuario import UsuarioCriacao, UsuarioResposta, TokenResposta
from ..servicos.autenticacao import (
    criar_hash_senha, 
    verificar_senha, 
    criar_token_acesso
)

roteador = APIRouter()

@roteador.post("/register", response_model=UsuarioResposta)
def registrar_usuario(
    usuario: UsuarioCriacao, 
    sessao: Session = Depends(obter_sessao_bd)
):
    """
    Endpoint para registro de novo usuário
    """
    # Verificar se usuário ou email já existem
    usuario_existente = sessao.query(Usuario).filter(
        (Usuario.usuario == usuario.usuario) | (Usuario.email == usuario.email)
    ).first()
    
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário ou email já cadastrado"
        )
    
    # Criar novo usuário
    novo_usuario = Usuario(
        usuario=usuario.usuario,
        email=usuario.email,
        senha_hash=criar_hash_senha(usuario.senha)
    )
    
    sessao.add(novo_usuario)
    sessao.commit()
    sessao.refresh(novo_usuario)
    
    return novo_usuario

@roteador.post("/login", response_model=TokenResposta)
def fazer_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    sessao: Session = Depends(obter_sessao_bd)
):
    """
    Endpoint para login de usuário
    """
    # Buscar usuário
    usuario = sessao.query(Usuario).filter(
        Usuario.usuario == form_data.username
    ).first()
    
    # Validar credenciais
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Criar token de acesso
    token_acesso = criar_token_acesso(
        dados={"sub": str(usuario.id)}
    )
    
    return {
        "access_token": token_acesso,
        "token_type": "bearer"
    }
