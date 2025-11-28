"""
API 路由详细模块
包含 users, items, login, private, utils 等业务路由
"""

from fastapi import APIRouter

from . import items, login, private, users, utils
from ..config import settings

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(utils.router)
api_router.include_router(items.router)


if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)


__all__ = ["api_router"]
