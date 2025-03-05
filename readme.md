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

