from fastapi import APIRouter

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
def get_all() -> list[EquipeSchema]:
    return equipe_service.get_all()


@router.get("/{id}", response_model=EquipeSchema, status_code=200)
def get_by_id(id: int) -> EquipeSchema:
    return equipe_service.get_by_id(id)


@router.put("/{id}", response_model=EquipeSchema, status_code=200)
def update(id: int, equipe: EquipeUpdateSchema) -> EquipeSchema:
    return equipe_service.update(id, equipe)


@router.delete("/{id}", status_code=204)
def delete(id: int) -> None:
    equipe_service.delete(id)
