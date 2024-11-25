from pydantic import BaseModel

from app.models.info_tabela import InfoTabela


class Equipe(BaseModel):
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int
    info_tabela: InfoTabela