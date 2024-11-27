from pydantic import BaseModel

from app.schemas.info_tabela_schema import InfoTabelaSchema


class EquipeCreateSchema(BaseModel):
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int
    info_tabela: InfoTabelaSchema

    class Config:
        from_attributes = True