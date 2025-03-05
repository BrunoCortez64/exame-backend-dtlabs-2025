from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..config import Configuracoes
from ..database import obter_sessao_bd
from ..modelos.usuario import Usuario
from ..esquemas.usuario import DadosToken

# Contexto de senha para hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema OAuth2 para autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def criar_hash_senha(senha: str) -> str:
    """
    Cria hash da senha usando bcrypt
    """
    return pwd_context.hash(senha)

def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    """
    Verifica se a senha plana corresponde ao hash
    """
    return pwd_context.verify(senha_plana, senha_hash)

def criar_token_acesso(dados: dict, expiracao: Optional[timedelta] = None):
    """
    Cria um token de acesso JWT
    """
    dados_copiar = dados.copy()
    
    if expiracao:
        expira = datetime.utcnow() + expiracao
    else:
        expira = datetime.utcnow() + timedelta(minutes=Configuracoes.TOKEN_EXPIRACAO_MINUTOS)
    
    dados_copiar.update({"exp": expira})
    
    return jwt.encode(
        dados_copiar, 
        Configuracoes.SECRET_KEY, 
        algorithm=Configuracoes.ALGORITHM
    )

def obter_usuario_atual(
    token: str = Depends(oauth2_scheme), 
    sessao: Session = Depends(obter_sessao_bd)
) -> Usuario:
    """
    Obtém o usuário atual a partir do token JWT
    """
    try:
        payload = jwt.decode(
            token, 
            Configuracoes.SECRET_KEY, 
            algorithms=[Configuracoes.ALGORITHM]
        )
        usuario_id: str = payload.get("sub")
        
        if usuario_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Não foi possível validar as credenciais",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        token_data = DadosToken(sub=usuario_id)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    usuario = sessao.query(Usuario).filter(Usuario.id == int(usuario_id)).first()
    
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return usuario
