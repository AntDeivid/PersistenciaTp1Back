from pydantic import BaseModel


class InfoTabelaSchema(BaseModel):
    id: int
    pontos: int
    jogos: int
    vitorias: int
    empates: int
    derrotas: int

    class Config:
        from_attributes = True