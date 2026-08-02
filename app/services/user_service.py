from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

class UserService:
    @staticmethod
    async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
        result = await session.execute(select(User).where(User.username == username))
        return result.scalars().first()

    @staticmethod
    async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalars().first()

    @staticmethod
    async def create_user(session: AsyncSession, user_create: UserCreate) -> User:
        existing_user = await UserService.get_user_by_username(session, user_create.username)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

        existing_email = await UserService.get_user_by_email(session, user_create.email)
        if existing_email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

        hashed_password = AuthService.get_password_hash(user_create.password)
        user = User(
            username=user_create.username,
            email=user_create.email,
            hashed_password=hashed_password,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def authenticate_user(session: AsyncSession, username: str, password: str) -> User | None:
        import logging
        log = logging.getLogger(__name__)
        user = await UserService.get_user_by_username(session, username)
        if not user:
            log.warning(f"LOGIN FAILED: user '{username}' not found in DB")
            return None
        if not AuthService.verify_password(password, user.hashed_password):
            log.warning(f"LOGIN FAILED: wrong password for user '{username}'")
            return None
        return user
