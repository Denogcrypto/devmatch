from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/discover", response_class=HTMLResponse)
async def discover(request: Request):
    return templates.TemplateResponse("discover.html", {"request": request})
