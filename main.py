from fastapi import FastAPI

from app.routers import equipe_router

app = FastAPI()


app.include_router(equipe_router.router, tags=["Equipes"], include_in_schema=True)
app.include_router(equipe_router.router, tags=["Equipes"], include_in_schema=True)