from mapper.object_mapper import ObjectMapper

from app.models.equipe import Equipe
from app.schemas.equipe_schema import EquipeSchema

mapper = ObjectMapper()

toSchema = {
    "info_tabela.id": "info_tabela_id"
}

toEntity = {
    "info_tabela_id": "info_tabela.id"
}

mapper.create_map(
    Equipe,
    EquipeSchema,
    toSchema
)

mapper.create_map(
    EquipeSchema,
    Equipe,
    toEntity
)