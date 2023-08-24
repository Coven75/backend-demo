from fastapi import APIRouter

from app.public.auth import auth_controller

router = APIRouter()


def public_api_routes():
    router.include_router(auth_controller.router)


public_api_routes()
