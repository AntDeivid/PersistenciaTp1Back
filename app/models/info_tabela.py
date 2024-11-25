from pydantic import BaseModel


class InfoTabela(BaseModel):
    pontos: int
    jogos: int
    vitorias: int
    empates: int
    derrotas: int