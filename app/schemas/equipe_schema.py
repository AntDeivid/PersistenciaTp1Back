from pydantic import BaseModel

from app.schemas.info_tabela_schema import InfoTabelaSchema


class EquipeSchema(BaseModel):
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int
    info_tabela: InfoTabelaSchema

    class Config:
        orm_mode = True