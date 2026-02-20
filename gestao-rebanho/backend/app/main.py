from fastapi import FastAPI, Request
from app.database import Base, engine
from app.routes import animal, registro_peso

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Gestão de Rebanho API",version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(animal.router)
app.include_router(registro_peso.router)


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


