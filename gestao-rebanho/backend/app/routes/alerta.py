from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.alerta import Alerta
from app.schemas.alerta import AlertaResponse
from app.services.alerta_service import verificar_vacinas, verificar_peso
from typing import List

router = APIRouter(prefix="/alertas", tags=["Alertas"])

@router.post("/gerar")
def gerar_alertas(db: Session = Depends(get_db)):
    verificar_vacinas(db)
    verificar_peso(db)
    return {"mensagem": "Alertas verificados com sucesso"}

@router.get("/", response_model=List[AlertaResponse])
def listar_alertas(db: Session = Depends(get_db)):
    return db.query(Alerta).filter(Alerta.resolvido == False).all()