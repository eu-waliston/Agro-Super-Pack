from fastapi import FastAPI
from app.database import Base, engine
from app.routes import animal, registro_peso

app = FastAPI(title="Gestão de Rebanho API")

Base.metadata.create_all(bind=engine)

app.include_router(animal.router)
app.include_router(registro_peso.router)

