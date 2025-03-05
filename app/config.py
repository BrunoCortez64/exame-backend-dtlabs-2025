import os
from dotenv import load_dotenv

load_dotenv()

class Configuracoes:
    # Configurações do banco de dados
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql://usuario:senha@localhost/bancoDados')
    
    # Configurações de autenticação JWT
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'suachavesecreta')
    ALGORITHM: str = os.getenv('ALGORITHM', 'HS256')
    TOKEN_EXPIRACAO_MINUTOS: int = 30

    # Outras configurações
    TEMPO_OFFLINE_SERVIDOR: int = 10  # segundos
