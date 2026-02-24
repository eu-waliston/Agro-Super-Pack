from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class AlertaResponse(BaseModel):
    id: UUID
    animal_id: UUID
    tipo: str
    nivel: str
    mensagem: set
    resolvido: bool
    data_criacao: datetime
    
    class Config:
        from_attributes = True