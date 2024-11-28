from pydantic import BaseModel

class InfoTabelaCreateSchema(BaseModel):
    pontos: int
    jogos: int
    vitorias: int
    empates: int
    derrotas: int

    class Config:
        from_attributes = True