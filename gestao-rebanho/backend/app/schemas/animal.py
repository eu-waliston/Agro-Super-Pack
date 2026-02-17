from pydantic import BaseModel
from datetime import date
from uuid import UUID
from enum import Enum

class EspeciaeEnum(str, Enum):
    bovino = "bovino"
    ovino = "ovino"
    caprino = "caprino"
    suino = "suino"

class SexoEnum(str, Enum):
    M = "M"
    F = "F"

class StatusEnum(str, Enum):
    ativo = "ativo"
    vendido = "vendido"
    doente = "doente"
    
class AnimalCreate(BaseModel):
    identificacao: str
    especie: EspeciaeEnum
    sexo: SexoEnum
    nascimento: date
    peso_atual: float
    
class AnimalResponse(BaseModel):
    id: UUID
    idenfiticacao: str
    especie: EspeciaeEnum
    sexo: SexoEnum
    nascimento: date
    peso_atual: float
    status: StatusEnum
    
    class Config:
        from_attributes = True