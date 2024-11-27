from pydantic import BaseModel


class EquipeSchema(BaseModel):
    id: int
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int
    info_tabela_id: int

    class Config:
        from_attributes = True