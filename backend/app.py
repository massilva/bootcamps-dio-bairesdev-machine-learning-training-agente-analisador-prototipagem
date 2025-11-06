from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.controllers.analisador import router as analisador_router

# Configuração do FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
PREFIXO_API = "/api/v1"
app.include_router(analisador_router, prefix=PREFIXO_API)
