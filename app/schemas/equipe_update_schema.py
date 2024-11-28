from pydantic import BaseModel


class EquipeUpdateSchema(BaseModel):
    id: int
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int