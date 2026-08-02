from fastapi import Request
from app.database import get_session

async def get_db():
    async for session in get_session():
        yield session

def get_current_username(request: Request) -> str | None:
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        from jose import jwt, JWTError
        from app.config import settings
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")
    except Exception:
        return None
