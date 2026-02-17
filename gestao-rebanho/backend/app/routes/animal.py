from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.animal import Animal
from app.schemas.animal import AnimalCreate, AnimalResponse
from typing import List

router = APIRouter(prefix="/animais", tags=["Animais"])

@router.post("/", response_model=AnimalResponse)
def criar_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    novo = Animal(**animal.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=List[AnimalResponse])
def listar_animais(db: Session = Depends(get_db)):
    return db.query(Animal).all()

@router.get("/{animal_id}", response_model=AnimalResponse)
def obter_animal(animal_id: str, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    
    if not animal:
        raise HTTPException(status_code=404, detail="Animal Não Encontrado!!")
    return animal


    
