from fastapi import APIRouter

from app.schemas.EquipeCreateSchema import EquipeCreateSchema
from app.schemas.equipe_schema import EquipeSchema
from app.services.equipe_service import EquipeService

router = APIRouter()
router.prefix = "/api/equipes"
equipe_service = EquipeService()

@router.post("/", response_model = EquipeSchema, status_code = 201)
def save(equipe: EquipeCreateSchema) -> EquipeSchema:
    return equipe_service.save(equipe)