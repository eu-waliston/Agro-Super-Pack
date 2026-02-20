from sqlalchemy import Column, String, Date, Float, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from sqlalchemy.orm import relationship
import uuid
import enum

class EspecieEnum(str, enum.Enum):
    bovino = "bovino"
    ovibo="ovino"
    caprino="suino"

class SexoEnum(str, enum.Enum):
    M = "M"
    F = "F"

class StatusEnum(str, enum.Enum):
    ativo = "ativo"
    vendido = "vendido"
    doente = "doente"

class Animal(Base):
    __tablename__ = "animais"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    identificacao = Column(String, unique=True, nullable=False)

    sexo = Column(Enum(SexoEnum), nullable=False)

    nascimento = Column(Date, nullable=False)

    peso_atual = Column(Float, nullable=False)

    status = Column(Enum(StatusEnum), default=StatusEnum.ativo)
    
    registros_peso = relationship(
        "RegistroPeso",
        back_populates="animal",
        cascade="all, delete"
    )
    
    aplicacao_vacina = relationship (
        "AplicacaoVacina",
        back_populates="animal",
        cascade="all, delete"
    )
