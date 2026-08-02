from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr

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
async def login_form(request: Request, registered: int | None = None):
    return templates.TemplateResponse("login.html", {"request": request, "registered": registered})

@router.post("/login", response_class=HTMLResponse)
async def login_form_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    session=Depends(get_db),
):
    user = await UserService.authenticate_user(session, username, password)
    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Usuario o contraseña incorrectos", "username": username},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="access_token", value=access_token, httponly=True, max_age=60 * 60 * 24)
    return response

@router.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register", response_class=HTMLResponse)
async def register_form_submit(
    request: Request,
    username: str = Form(...),
    email: EmailStr = Form(...),
    password: str = Form(...),
    session=Depends(get_db),
):
    user_create = UserCreate(username=username, email=email, password=password)
    try:
        await UserService.create_user(session, user_create)
    except HTTPException as exc:
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "error": exc.detail,
                "username": username,
                "email": email,
            },
            status_code=exc.status_code,
        )

    return RedirectResponse(url="/login?registered=1", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("access_token")
    return response
