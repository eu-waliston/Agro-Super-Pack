from sqlalchemy import Column, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class AplicarVacina(Base):
    __tablename__ = "aplicacoes_vacina"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    animal_id = Column(UUID(as_uuid=True), ForeignKey("animais.id", ondelete="CASCADE"), nullable=False)
    
    vacina_id = Column(UUID(as_uuid=True), ForeignKey("vacinas.id"), nullable=False)
    
    data_aplicacao = Column(Date, nullable=False)
    
    proxima_dose = Column(Date, nullable=False)
    
    animal = relationship("Animal", back_populates="aplicacao_vacina")
    vacina = relationship("Vacina")
    
