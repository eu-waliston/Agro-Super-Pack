from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List

from app.models.alerta import Alerta
from app.schemas.alerta import AlertaResponse
from app.services.alerta_service import verificar_vacinas, verificar_peso, processar_alertas


router = APIRouter(prefix="/alertas", tags=["Alertas"])

@router.post("/gerar")
def gerar_alertas(db: Session = Depends(get_db)):
    verificar_vacinas(db)
    verificar_peso(db)
    return {"mensagem": "Alertas verificados com sucesso"}

@router.get("/", response_model=List[AlertaResponse])
def listar_alertas(db: Session = Depends(get_db)):
    return db.query(Alerta).filter(Alerta.resolvido == False).all()

@router.patch("/{alerta_id}/resolve")
def resolver_alerta(alerta_id: int, db: Session = Depends(get_db)):
    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).first()
    
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta não encontrado")
    
    alerta.resolvido = bool(True) # type: ignore
    alerta.data_resolucao = datetime.utcnow()
    
    db.commit()
    
    return {"mensagem": "Alerta resolvido"}
    
@router.post("/check")
def verificar_alertas(backgroundTasks: BackgroundTasks, db: Session = Depends(get_db)):
    backgroundTasks.add_task(processar_alertas,db)
    return {"message": "verificação iniciada"}

@router.get("/count")
def contar_alertas(db: Session = Depends(get_db)):
    
    total = db.query(Alerta).filter(
        Alerta.resolvido == False
    ).count()
    
    criticos = db.query(Alerta).filter(
        Alerta.resolvido == False,
        Alerta.nivel == "CRITICO"
    ).count()
    
    return {
        "total_ativos": total,
        "total_criticos": criticos
    }