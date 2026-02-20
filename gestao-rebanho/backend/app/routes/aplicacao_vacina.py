# app/routes/aplicacao_vacina.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.animal import Animal
from app.models.vacina import Vacina
from app.models.aplicacao_vacina import AplicarVacina
from app.schemas.aplicacao_vacina import AplicacaoCreate, AplicacaoResponse
from datetime import timedelta
from typing import List
from uuid import UUID

router = APIRouter(prefix="/animais", tags=["Aplicações de Vacina"])


@router.post("/{animal_id}/vacinas", response_model=AplicacaoResponse)
def aplicar_vacina(
    animal_id: UUID,
    dados: AplicacaoCreate,
    db: Session = Depends(get_db)
):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")

    vacina = db.query(Vacina).filter(Vacina.id == dados.vacina_id).first()
    if not vacina:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")

    proxima = dados.data_aplicacao + timedelta(days=vacina.intervalo_dias)

    aplicacao = AplicacaoVacina(
        animal_id=animal_id,
        vacina_id=dados.vacina_id,
        data_aplicacao=dados.data_aplicacao,
        proxima_dose=proxima
    )

    db.add(aplicacao)
    db.commit()
    db.refresh(aplicacao)

    return aplicacao


@router.get("/{animal_id}/vacinas", response_model=List[AplicacaoResponse])
def listar_vacinas_animal(animal_id: UUID, db: Session = Depends(get_db)):
    return (
        db.query(AplicacaoVacina)
        .filter(AplicacaoVacina.animal_id == animal_id)
        .all()
    )