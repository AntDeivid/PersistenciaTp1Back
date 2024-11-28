from typing import Optional

from pydantic import BaseModel

from app.schemas.info_tabela_schema import InfoTabelaSchema


class EquipeSchema(BaseModel):
    id: int
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int
    info_tabela: Optional[InfoTabelaSchema] = None

    class Config:
        from_attributes = True