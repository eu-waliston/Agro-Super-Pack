from sqlalchemy import Column,Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid
from datetime import datetime

class Alerta(Base):
    __tablename__ = "alerta"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    animal_id = Column(UUID(as_uuid=True), ForeignKey("animais.id", ondelete="CASCADE"), nullable=False)
    
    tipo = Column(String, nullable=False) # vacina_vencida | peso_baixo | etc
    nivel = Column(String, nullable=False) # info | warning | critical
    mensagem = Column(String, nullable=False)
    
    resolvido = Column(Boolean, default=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    
    animal = relationship("Animal")
    

class Alertas(Base):
    __tablename__ = "alertas"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(UUID(as_uuid=True), ForeignKey("animais.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(String)
    mensagem = Column(String)
    nivel = Column(String, default="MODERADO")
    
    resolvido = Column(Boolean, default=False)
    data_resolucao = Column(DateTime, nullable=False)
    
    criado_em = Column(DateTime, default=datetime.utcnow)

