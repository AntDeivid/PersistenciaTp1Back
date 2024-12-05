import logging.config

import yaml
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import equipe_router
from app.routers import info_tabela_router

app = FastAPI()

with open("logging_config.yaml", "r") as file:
    logging_config = yaml.safe_load(file)
    logging.config.dictConfig(logging_config)

app.include_router(equipe_router.router, tags=["Equipes"], include_in_schema=True)
app.include_router(info_tabela_router.router, tags=["InfoTabela"], include_in_schema=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)