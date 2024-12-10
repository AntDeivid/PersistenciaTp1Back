from fastapi import APIRouter, HTTPException

from app.schemas.InfoTabelaCreateSchema import InfoTabelaCreateSchema
from app.schemas.info_tabela_schema import InfoTabelaSchema
from app.services.info_tabela_service import InfoTabelaService

router = APIRouter()
router.prefix = "/api/info_tabela"
info_tabela_service = InfoTabelaService()

@router.post("/", response_model = InfoTabelaSchema, status_code = 201)
def save(info_tabela: InfoTabelaCreateSchema) -> InfoTabelaSchema:
    return info_tabela_service.save(info_tabela)

@router.get("/", response_model = list[InfoTabelaSchema])
def get_all() -> list[InfoTabelaSchema]:
    return info_tabela_service.get_all()

@router.get("/{id}", response_model = InfoTabelaSchema)
def get_by_id(id: int) -> InfoTabelaSchema:
    return info_tabela_service.get_by_id(id)

@router.put("/{id}", response_model=InfoTabelaCreateSchema)
def update(id: int, info_tabela: InfoTabelaCreateSchema):
    return info_tabela_service.update(id, info_tabela)

@router.delete("/{id}", status_code = 204)
def delete(id: int) -> None:
    info_tabela_service.delete(id)
    