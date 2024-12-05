from app.models.info_tabela import InfoTabela
from app.schemas.InfoTabelaCreateSchema import InfoTabelaCreateSchema
from app.schemas.info_tabela_schema import InfoTabelaSchema


class InfoTabelaMapper:

    @staticmethod
    def to_schema(info_tabela: InfoTabela) -> InfoTabelaSchema:
        return InfoTabelaSchema(
            id=info_tabela.id,
            pontos=info_tabela.pontos,
            jogos=info_tabela.jogos,
            vitorias=info_tabela.vitorias,
            empates=info_tabela.empates,
            derrotas=info_tabela.derrotas,
        )

    @staticmethod
    def to_entity(info_tabela_schema: InfoTabelaSchema, info_tabela_id: int) -> InfoTabela:
        return InfoTabela(
            id=info_tabela_id,
            pontos=info_tabela_schema.pontos,
            jogos=info_tabela_schema.jogos,
            vitorias=info_tabela_schema.vitorias,
            empates=info_tabela_schema.empates,
            derrotas=info_tabela_schema.derrotas,
        )

    @staticmethod
    def create_to_entity(info_tabela_schema: InfoTabelaCreateSchema, info_tabela_id: int) -> InfoTabela:
        return InfoTabela(
            id=info_tabela_id,
            pontos=info_tabela_schema.pontos,
            jogos=info_tabela_schema.jogos,
            vitorias=info_tabela_schema.vitorias,
            empates=info_tabela_schema.empates,
            derrotas=info_tabela_schema.derrotas,
        )