from app.mappers.info_tabela_mapper import InfoTabelaMapper
from app.repositories.info_tabela_repository import InfoTabelaRepository
from app.schemas.info_tabela_schema import InfoTabelaSchema
from app.schemas.InfoTabelaCreateSchema import InfoTabelaCreateSchema
from app.models.info_tabela import InfoTabela


from app.mappers.info_tabela_mapper import InfoTabelaMapper
from app.repositories.info_tabela_repository import InfoTabelaRepository
from app.schemas.info_tabela_schema import InfoTabelaSchema
from app.models.info_tabela import InfoTabela


class InfoTabelaService:
    def __init__(self):
        self.info_tabela_repository = InfoTabelaRepository()

    def save(self, info_tabela: InfoTabelaSchema) -> InfoTabela:
        info_tabela_id = self.info_tabela_repository.get_next_id()
        if not isinstance(info_tabela_id, (int, float)) or info_tabela_id is None or info_tabela_id != info_tabela_id:  
            raise ValueError("Invalid ID generated")
        new_info_tabela = InfoTabelaMapper.to_entity(info_tabela, info_tabela_id)
        saved_info_tabela = self.info_tabela_repository.save(new_info_tabela)
        return saved_info_tabela
    
    def get_by_id(self, info_tabela_id: int) -> InfoTabela:
        return self.info_tabela_repository.get_by_id(info_tabela_id)

    def get_all(self) -> list[InfoTabela]:
        return self.info_tabela_repository.get_all()
    
    def update(self, id: int, info_tabela: InfoTabelaCreateSchema) -> InfoTabela:
        info_tabela_entity = InfoTabelaMapper.to_entity(info_tabela, id)
        return self.info_tabela_repository.update(info_tabela_entity)
    
    def delete(self, info_tabela_id: int) -> None:
        self.info_tabela_repository.delete(info_tabela_id)