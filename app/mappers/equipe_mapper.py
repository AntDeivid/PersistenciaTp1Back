from app.models.equipe import Equipe
from app.schemas.EquipeCreateSchema import EquipeCreateSchema
from app.schemas.equipe_schema import EquipeSchema
from app.schemas.equipe_update_schema import EquipeUpdateSchema


class EquipeMapper:

    @staticmethod
    def to_schema(equipe: Equipe) -> EquipeSchema:
        return EquipeSchema(
            id=equipe.id,
            nome=equipe.nome,
            estadio=equipe.estadio,
            apelido=equipe.apelido,
            jogadores_registrados=equipe.jogadores_registrados,
        )

    @staticmethod
    def to_entity(equipe_schema: EquipeUpdateSchema, equipe_id: int, info_tabela_id: int) -> Equipe:
        equipe = Equipe(
            id=equipe_id,
            nome=equipe_schema.nome,
            estadio=equipe_schema.estadio,
            apelido=equipe_schema.apelido,
            jogadores_registrados=equipe_schema.jogadores_registrados,
            info_tabela_id=info_tabela_id,
        )

        return equipe

    @staticmethod
    def create_to_entity(equipe_create_schema: EquipeCreateSchema, equipe_id: int, info_tabela: int) -> Equipe:
        equipe = Equipe(
            id=equipe_id,
            nome=equipe_create_schema.nome,
            estadio=equipe_create_schema.estadio,
            apelido=equipe_create_schema.apelido,
            jogadores_registrados=equipe_create_schema.jogadores_registrados,
            info_tabela_id=info_tabela,
        )

        return equipe