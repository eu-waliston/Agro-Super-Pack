from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class Vacina(Base):
    __tablename__ = "vacinas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(String)
    intervalo_dias = Column(Integer, nullable=False)  # intervalo para próxima dose