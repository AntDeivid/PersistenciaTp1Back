from pydantic import BaseModel


class InfoTabelaSchema(BaseModel):
    pontos: int
    jogos: int
    vitorias: int
    empates: int
    derrotas: int

    class Config:
        orm_mode = True