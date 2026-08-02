from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routes import auth_router, dashboard_router, discover_router, profile_router, matches_router
from app.routes.health import router as health_router
from app.database import init_db

app = FastAPI(title="DevMatch")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(discover_router)
app.include_router(profile_router)
app.include_router(matches_router)
app.include_router(health_router)
