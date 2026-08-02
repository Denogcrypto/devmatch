from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.schemas.user import UserCreate, UserRead
from app.schemas.token import Token
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.utils.dependencies import get_db
from app.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/auth/register", response_model=UserRead)
async def register(user_create: UserCreate, session=Depends(get_db)):
    return await UserService.create_user(session, user_create)

@router.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session=Depends(get_db)):
    user = await UserService.authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
