# Configurações do Banco de Dados PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=bancoDados
POSTGRES_USER=usuario_desenvolvimento
POSTGRES_PASSWORD=sua_senha_secreta_aqui

# URL de conexão com o banco de dados
DATABASE_URL=postgresql://usuario_desenvolvimento:sua_senha_secreta_aqui@localhost:5432/bancoDados

# Configurações de Autenticação JWT
SECRET_KEY=sua_chave_secreta_de_32_caracteres_aqui
ALGORITHM=HS256
TOKEN_EXPIRATION_MINUTES=30

# Configurações de Ambiente
ENVIRONMENT=development
DEBUG=True

# Configurações de Logs
LOG_LEVEL=DEBUG

# Configurações de Segurança
PASSWORD_MIN_LENGTH=8
MAX_LOGIN_ATTEMPTS=5

# Configurações de Rate Limiting
REQUEST_RATE_LIMIT=100
REQUEST_RATE_PERIOD=60

# Configurações de Sensores
MAX_SENSOR_FREQUENCY=10
OFFLINE_THRESHOLD_SECONDS=10

# Configurações Opcionais de Cache
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

