from fastapi import FastAPI, Request
from app.database import Base, engine, SessionLocal
from app.routes import animal, registro_peso
from app.routes import vacina, aplicacao_vacina
from app.routes import alerta
from apscheduler.schedulers.background import BackgroundScheduler

from app.services.alerta_service import processar_alertas

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Gestão de Rebanho API",version="1.0.0")


Base.metadata.create_all(bind=engine)

app.include_router(animal.router)
app.include_router(registro_peso.router)
app.include_router(vacina.router)
app.include_router(aplicacao_vacina.router)
app.include_router(alerta.router)

# Templates
templates = Jinja2Templates(directory="templates")

# Arquivos estáticos (images, css, etc)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint de status
app.get("/status")
def status():
    return {"status": "online"}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": app.title,
            "version": app.version
        }
    )

scheduler = BackgroundScheduler()

def job_alertas():
    db = SessionLocal()
    try:
        processar_alertas(db)
    finally:
        db.close()
        
scheduler.add_job(job_alertas, "interval", hours=24)
scheduler.start()

