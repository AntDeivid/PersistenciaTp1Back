from pydantic import BaseModel

from app.schemas.InfoTabelaCreateSchema import InfoTabelaCreateSchema


class EquipeCreateSchema(BaseModel):
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int
    info_tabela: InfoTabelaCreateSchema

    class Config:
        from_attributes = True