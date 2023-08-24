from typing import Annotated

import objgraph
from fastapi import APIRouter, Depends

from app.admin.user.admin_user_service import AdminUserService, get_admin_user_service
from core.model.common_query_params import CommonQueryParams
from dependencies.dependencies import get_user_translations, get_current_user
from core.model.response_api import ResponseApi, Level

router = APIRouter(
    prefix="/admin-user",
    tags=["admin-user"],
    responses={404: {"description": "Not found"}},
)

service = get_admin_user_service()


@router.get("")
async def get_users(commons: Annotated[CommonQueryParams, Depends()],
                    current_user=Depends(get_current_user),
                    translations=Depends(get_user_translations)):
    user = service.get_user_list(commons, current_user)
    return ResponseApi(
        message=translations.get('user_not_found'),
        level=Level.success
    )
