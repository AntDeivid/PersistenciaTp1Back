from app.mappers.equipe_mapper import EquipeMapper
from app.mappers.info_tabela_mapper import InfoTabelaMapper
from app.repositories.equipe_repository import EquipeRepository
from app.repositories.info_tabela_repository import InfoTabelaRepository
from app.schemas.EquipeCreateSchema import EquipeCreateSchema
from app.schemas.equipe_schema import EquipeSchema


class EquipeService:

    def __init__(self):
        self.equipe_repository = EquipeRepository()
        self.info_tabela_repository = InfoTabelaRepository()

    def save(self, equipe: EquipeCreateSchema) -> EquipeSchema:
        equipe_id = self.equipe_repository.get_next_id()
        info_tabela_id = self.info_tabela_repository.get_next_id()

        new_equipe = EquipeMapper.create_to_entity(equipe, equipe_id, info_tabela_id)
        new_info_tabela = InfoTabelaMapper.to_entity(equipe.info_tabela, info_tabela_id)

        self.info_tabela_repository.save(new_info_tabela)
        saved_equipe = self.equipe_repository.save(new_equipe)

        return EquipeMapper.to_schema(saved_equipe)