from pydantic import BaseModel
from uuid import UUID

class VacinaCreate(BaseModel):
    nome: str
    descricao: str | None = None
    intervalo_dias: int

class VacinaRespose(BaseModel):
    id: UUID
    nome: str
    descricao: str | None
    intervalo_dias: int
    
    class Config:
        from_attributes = True