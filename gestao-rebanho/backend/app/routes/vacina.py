from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.vacina import Vacina
from app.schemas.vacina import VacinaCreate, VacinaRespose
from typing import List

router = APIRouter(prefix="/vacinas", tags=["Vacinas"])

@router.post("/", response_model=VacinaRespose)
def criar_vacina(dados: VacinaCreate, db: Session = Depends(get_db)):
    vacina = Vacina(**dados.model_dump())
    db.add(vacina)
    db.commit()
    db.refresh(vacina)
    return vacina

@router.get("/", response_model=List[VacinaRespose])
def listar_vacinas(db: Session = Depends(get_db)):
    return db.query(Vacina).all()

