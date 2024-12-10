from typing import Optional

from fastapi import APIRouter
from starlette.responses import StreamingResponse

from app.FilterType import FilterType
from app.schemas.EquipeCreateSchema import EquipeCreateSchema
from app.schemas.equipe_schema import EquipeSchema
from app.schemas.equipe_update_schema import EquipeUpdateSchema
from app.services.equipe_service import EquipeService

router = APIRouter()
router.prefix = "/api/equipes"
equipe_service = EquipeService()


@router.post("/", response_model=EquipeSchema, status_code=201)
def save(equipe: EquipeCreateSchema) -> EquipeSchema:
    return equipe_service.save(equipe)


@router.get("/", response_model=list[EquipeSchema], status_code=200)
def get_all(filter_equipe: Optional[FilterType] = None) -> list[EquipeSchema]:
    return equipe_service.get_all(filter_equipe)


@router.get("/count-entities", response_model=int, status_code=200)
def count_entities() -> int:
    return equipe_service.count_lines()


@router.get("/export", status_code=200)
def export() -> StreamingResponse:
    return equipe_service.get_zip_file()


@router.get("/search", response_model=list[EquipeSchema], status_code=200)
def get_with_search(search: str) -> list[EquipeSchema]:
    return equipe_service.get_with_search(search)


@router.get("/file-hash", response_model=dict[str, str], status_code=200)
def get_file_hash() -> dict[str, str]:
    return {"hash": equipe_service.get_file_hash()}


@router.get("/{id}", response_model=EquipeSchema, status_code=200)
def get_by_id(id: int) -> EquipeSchema:
    return equipe_service.get_by_id(id)


@router.put("/{id}", response_model=EquipeSchema, status_code=200)
def update(id: int, equipe: EquipeUpdateSchema) -> EquipeSchema:
    return equipe_service.update(id, equipe)


@router.delete("/{id}", status_code=204)
def delete(id: int) -> None:
    equipe_service.delete(id)
