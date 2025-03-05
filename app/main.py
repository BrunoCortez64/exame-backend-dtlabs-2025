from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .rotas import autenticacao, servidores, dados, saude

app = FastAPI(
    title="Exame Backend DTLabs",
    description="API para gerenciamento de dados de sensores IoT",
    version="1.0.0"
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir roteadores
app.include_router(autenticacao.roteador, prefix="/auth", tags=["Autenticação"])
app.include_router(servidores.roteador, prefix="/servers", tags=["Servidores"])
app.include_router(dados.roteador, prefix="/data", tags=["Dados de Sensores"])
app.include_router(saude.roteador, prefix="/health", tags=["Saúde do Servidor"])

@app.get("/")
async def raiz():
    return {"mensagem": "Bem-vindo à API de Sensores IoT"}
