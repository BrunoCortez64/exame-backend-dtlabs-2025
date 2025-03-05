# Exame Backend DTLabs 2025

## Descrição do Projeto
Sistema de backend para gerenciamento de dados de sensores IoT, desenvolvido com FastAPI, PostgreSQL e Docker.

## Requisitos
- Python 3.11+
- Docker
- Docker Compose

## Configuração do Ambiente

### Variáveis de Ambiente
Crie um arquivo `.env` com as seguintes variáveis:
```
DATABASE_URL=postgresql://usuario:senha@localhost/bancoDados
SECRET_KEY=suachavesecreta
ALGORITHM=HS256
```

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/BrunoCortez64/exame-backend-dtlabs-2025.git
cd exame-backend-dtlabs-2025
```

2. Construa e inicie os containers:
```bash
docker-compose up --build
```

## Executando Testes
```bash
docker-compose run backend pytest
```

## Documentação da API
Acesse a documentação Swagger em: `http://localhost:8000/docs`

## Endpoints
- `/auth/register`: Registro de usuário
- `/auth/login`: Autenticação
- `/data`: Registro e consulta de dados de sensores
- `/servers`: Registro de servidores
- `/health/{server_id}`: Status de saúde do servidor

## Tecnologias
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT para autenticação
- Docker
- PyTest

## Resumo do Projeto
🔐 Componentes Detalhados
1. Autenticação (JWT)

Registro de usuários
Login com geração de token
Proteção de endpoints
Hashing de senhas com bcrypt

2. Modelos de Dados
Usuário

Campos: id, usuário, email, senha_hash
Geração de ULID único
Relacionamento com servidores

Servidor

Campos: id, ulid, nome, usuário_id
Rastreamento do último dado recebido
Relacionamento com dados de sensores

Dados do Sensor

Campos: timestamp, temperatura, umidade, tensão, corrente
Relacionamento com servidor

3. Endpoints
Autenticação

POST /auth/register: Criar novo usuário
POST /auth/login: Autenticar e gerar token

Servidores

POST /servers: Registrar novo servidor
GET /health/{server_id}: Verificar status do servidor
GET /health/all: Listar status de todos os servidores

Dados de Sensor

POST /data: Registrar dados de sensores
GET /data: Consultar dados com filtros

4. Configuração de Banco de Dados

Uso do PostgreSQL via SQLAlchemy
Conexão configurável via variáveis de ambiente
Pool de conexões otimizado
Criação automática de banco de dados

5. Segurança

Senhas hashadas
Tokens JWT com expiração
Validações de entrada
Proteção contra criação de dados inválidos

6. Containerização

Docker Compose para ambiente de desenvolvimento
Serviços separados para backend e banco de dados
Configuração de healthcheck

7. Testes

Estrutura preparada para testes com PyTest
Cobertura para rotas e serviços

