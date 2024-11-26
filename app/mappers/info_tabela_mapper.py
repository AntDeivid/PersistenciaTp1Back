from mapper.object_mapper import ObjectMapper

from app.models.info_tabela import InfoTabela
from app.schemas.info_tabela_schema import InfoTabelaSchema

mapper = ObjectMapper()

mapper.create_map(InfoTabela, InfoTabelaSchema)

mapper.create_map(InfoTabelaSchema, InfoTabela)