from app.routes.auth import router as auth_router
from app.routes.dashboard import router as dashboard_router
from app.routes.discover import router as discover_router
from app.routes.profile import router as profile_router
from app.routes.matches import router as matches_router

__all__ = ["auth_router", "dashboard_router", "discover_router", "profile_router", "matches_router"]
