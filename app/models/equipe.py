from pydantic import BaseModel

class Equipe(BaseModel):
    id: int
    nome: str
    estadio: str
    apelido: str
    jogadores_registrados: int
    info_tabela_id: int