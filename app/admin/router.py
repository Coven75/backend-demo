from fastapi import APIRouter

from app.admin.user import admin_user_controller

router = APIRouter()


def admin_api_routes():
    router.include_router(admin_user_controller.router)


admin_api_routes()
