from pydantic import BaseModel


class InfoTabela(BaseModel):
    id: int
    pontos: int
    jogos: int
    vitorias: int
    empates: int
    derrotas: int