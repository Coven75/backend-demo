from fastapi import APIRouter, Response, Depends
from jose import jwt
from passlib.context import CryptContext

from app.public.auth.api.me_api import MeApi
from app.public.auth.api.sign_in_api import SignInApi
from config import settings
from core.model.response_api import ResponseApi, Level
from database.database import database
from dependencies.dependencies import get_current_user, get_user_translations
from models.core.user_model import UserModel

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/sign-in")
async def sign_in(body: SignInApi, response: Response):
    user = UserModel(**database.get_collection('user').find_one(
        {'email': body.email, 'archived': False}
    ))

    if user is None:
        response.status_code = 401
        return ResponseApi(
            message='User not found',
            level=Level.error
        )

    if not __verify_password__(body.password, user.password):
        response.status_code = 401
        return ResponseApi(
            message='Password is incorrect',
            level=Level.error
        )

    if user.tenants is None or len(user.tenants) == 0:
        response.status_code = 401
        return ResponseApi(
            message='User has no tenants',
            level=Level.error
        )

    if user.currentTenant is None:
        user.currentTenant = user.tenants[0]

    response.set_cookie(key=settings.COOKIE_NAME, value=__create_access_token__(user), httponly=True)

    return ResponseApi(
        message='User logged in successfully',
        level=Level.success
    )


@router.get("/me")
async def me(current_user=Depends(get_current_user), translations=Depends(get_user_translations)):
    return ResponseApi(
        data=MeApi.to_api(current_user.user),
        message=translations.get('user_not_found'),
        level=Level.success
    )


def __verify_password__(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def __create_access_token__(user: UserModel):
    return jwt.encode({
        'userId': str(user.id),
        'currentTenantId': str(user.currentTenant.id),
    }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
