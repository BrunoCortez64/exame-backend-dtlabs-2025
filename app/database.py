from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import Configuracoes

# Criar engine de conexão
engine = create_engine(Configuracoes.DATABASE_URL)

# Criar sessão para interações com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos de banco de dados
Base = declarative_base()

def obter_sessao_bd():
    """
    Função para obter uma sessão de banco de dados.
    Será usada como dependência em rotas do FastAPI.
    """
    sessao = SessionLocal()
    try:
        yield sessao
    finally:
        sessao.close()
