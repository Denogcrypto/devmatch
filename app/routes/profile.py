from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})
