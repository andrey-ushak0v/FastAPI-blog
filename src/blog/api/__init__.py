from fastapi import APIRouter

from .posts import router as posts_router
from .auth import roter as auth_router

router = APIRouter()
router.include_router(posts_router)
router.include_router(auth_router)
