# app/schemas/registro_peso.py

from pydantic import BaseModel
from datetime import date
from uuid import UUID

class RegistroPesoCreate(BaseModel):
    peso: float
    data_registro: date

class RegistroPesoResponse(BaseModel):
    id: UUID
    animal_id: UUID
    peso: float
    data_registro: date

    class Config:
        from_attributes = True
