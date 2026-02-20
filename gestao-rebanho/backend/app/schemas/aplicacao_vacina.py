from pydantic import BaseModel
from datetime import date
from uuid import UUID

class AplicacaoCreate(BaseModel):
    vacina_id: UUID
    data_aplicacao: date
    
class AplicacaoResponse(BaseModel):
    id: UUID
    animal_id: UUID
    vacina_id: UUID
    data_aplicacao: date
    proxima_dose: date
    
    class Config:
        from_attributes = True