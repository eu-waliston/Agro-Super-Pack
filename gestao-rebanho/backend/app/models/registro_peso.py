from sqlalchemy import Column, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class RegistroPeso(Base):
    __tablename__ = "registros_peso"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    animal_id = Column(UUID(as_uuid=True), ForeignKey("animais.id", ondelete="CASCADE"), nullable=False)
    peso = Column(Float, nullable=False)
    data_registro = Column(Date, nullable=False)

    animal = relationship("Animal", back_populates="registros_peso")

