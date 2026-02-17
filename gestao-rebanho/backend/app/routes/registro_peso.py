# app/routes/registro_peso.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.animal import Animal
from app.models.registro_peso import RegistroPeso
from app.schemas.registro_peso import RegistroPesoCreate, RegistroPesoResponse
from typing import List
from uuid import UUID

router = APIRouter(prefix="/animais", tags=["Registro de Peso"])


@router.post("/{animal_id}/pesos", response_model=RegistroPesoResponse)
def registrar_peso(
    animal_id: UUID,
    dados: RegistroPesoCreate,
    db: Session = Depends(get_db)
):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()

    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")

    novo_registro = RegistroPeso(
        animal_id=animal_id,
        peso=dados.peso,
        data_registro=dados.data_registro
    )

    db.add(novo_registro)

    # 🔥 Atualiza automaticamente peso_atual
    animal.peso_atual = dados.peso

    db.commit()
    db.refresh(novo_registro)

    return novo_registro


@router.get("/{animal_id}/pesos", response_model=List[RegistroPesoResponse])
def listar_pesos(animal_id: UUID, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()

    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")

    return (
        db.query(RegistroPeso)
        .filter(RegistroPeso.animal_id == animal_id)
        .order_by(RegistroPeso.data_registro.desc())
        .all()
    )
