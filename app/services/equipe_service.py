from io import BytesIO
from zipfile import ZipFile

from starlette.responses import StreamingResponse

from app.mappers.equipe_mapper import EquipeMapper
from app.mappers.info_tabela_mapper import InfoTabelaMapper
from app.repositories.equipe_repository import EquipeRepository
from app.repositories.info_tabela_repository import InfoTabelaRepository
from app.schemas.EquipeCreateSchema import EquipeCreateSchema
from app.schemas.equipe_schema import EquipeSchema
from app.schemas.equipe_update_schema import EquipeUpdateSchema


class EquipeService:

    def __init__(self):
        self.equipe_repository = EquipeRepository()
        self.info_tabela_repository = InfoTabelaRepository()

    def save(self, equipe: EquipeCreateSchema) -> EquipeSchema:
        equipe_id = self.equipe_repository.get_next_id()
        info_tabela_id = self.info_tabela_repository.get_next_id()

        new_equipe = EquipeMapper.create_to_entity(equipe, equipe_id, info_tabela_id)
        new_info_tabela = InfoTabelaMapper.to_entity(equipe.info_tabela, info_tabela_id)

        saved_info_tabela = self.info_tabela_repository.save(new_info_tabela)
        saved_equipe = self.equipe_repository.save(new_equipe)

        schema = EquipeMapper.to_schema(saved_equipe)
        schema.info_tabela = InfoTabelaMapper.to_schema(saved_info_tabela)

        return schema

    def get_all(self) -> list[EquipeSchema]:
        entities = self.equipe_repository.get_all()
        schemas = []
        for entity in entities:
            schema = EquipeMapper.to_schema(entity)
            info_tabela = self.info_tabela_repository.get_by_id(entity.info_tabela_id)
            schema.info_tabela = InfoTabelaMapper.to_schema(info_tabela)
            schemas.append(schema)

        return schemas

    def get_by_id(self, id: int) -> EquipeSchema | None:
        equipe = self.equipe_repository.get_by_id(id)
        if equipe:
            schema = EquipeMapper.to_schema(equipe)
            info_tabela = self.info_tabela_repository.get_by_id(equipe.info_tabela_id)
            schema.info_tabela = InfoTabelaMapper.to_schema(info_tabela)
            return schema
        return None

    def get_with_search(self, search: str) -> list[EquipeSchema]:
        entities = self.equipe_repository.get_with_search(search)
        schemas = []
        for entity in entities:
            schema = EquipeMapper.to_schema(entity)
            info_tabela = self.info_tabela_repository.get_by_id(entity.info_tabela_id)
            schema.info_tabela = InfoTabelaMapper.to_schema(info_tabela)
            schemas.append(schema)

        return schemas

    def update(self, equipe_id: int, equipe: EquipeUpdateSchema) -> EquipeSchema:
        equipe_entity = self.equipe_repository.get_by_id(equipe_id)
        if equipe_entity:
            new_equipe = EquipeMapper.to_entity(equipe, equipe_id, equipe_entity.info_tabela_id)
            updated_equipe = self.equipe_repository.update(equipe_id, new_equipe)

            info_tabela = self.info_tabela_repository.get_by_id(updated_equipe.info_tabela_id)
            schema = EquipeMapper.to_schema(updated_equipe)
            schema.info_tabela = InfoTabelaMapper.to_schema(info_tabela)

            return schema

    def delete(self, id: int) -> None:
        equipe = self.equipe_repository.get_by_id(id)
        if equipe:
            self.equipe_repository.delete(id)
            self.info_tabela_repository.delete(equipe.info_tabela_id)

    def count_lines(self) -> int:
        return self.equipe_repository.count_lines()

    def get_zip_file(self) -> StreamingResponse:
        equipe_file_path = self.equipe_repository.get_file_path()
        info_tabela_file_path = self.info_tabela_repository.get_file_path()
        buffer = BytesIO()

        with ZipFile(buffer, 'w') as zip_file:
            zip_file.write(equipe_file_path, equipe_file_path)
            zip_file.write(info_tabela_file_path, info_tabela_file_path)
        buffer.seek(0)

        return StreamingResponse(content=iter([buffer.getvalue()]),
                                 media_type='application/x-zip-compressed',
                                 headers={'Content-Disposition': 'attachment; filename=equipes.zip'})