from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.observability.logger import configure_logging
from app.observability.telemetry import setup_telemetry
from app.routes.search_routes import router as search_router

configure_logging()

app = FastAPI(
    title="Comparação de Algoritmos de Busca em Strings - N2",
    description="Aplicação evoluída com Strategy, SearchResult, logs, métricas, traces e dashboard.",
    version="2.0.0",
)

setup_telemetry(app)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.include_router(search_router)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "service": "string-search-n2"}
