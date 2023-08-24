import logging

from babel.support import Translations
from bson import ObjectId
from fastapi import FastAPI, Request, Depends, HTTPException
from jose import JWTError, jwt

from config import settings
from core.model.context_data import ContextData
from database.database import database
from plugins.translation import get_translation, translations_cache


def get_current_user(request: Request) -> ContextData:
    token = request.cookies.get(settings.COOKIE_NAME)
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    jwt_payload = __decode_access_token__(token)

    user = database.get_collection('user').find_one({'_id': ObjectId(jwt_payload.get('userId'))})
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    tenant = database.get_collection('tenant').find_one({'_id': ObjectId(jwt_payload.get('currentTenantId'))})
    return ContextData(user=user, currentTenant=tenant)


def get_user_translations(current_user=Depends(get_current_user)):
    return get_translation(current_user.user.language.name.lower())


def __decode_access_token__(token: str):
    try:
        jwt_payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
    except JWTError as e:
        logging.error("ERR 4651: Cannot decode jwt token -> " + str(e))
        raise HTTPException(status_code=401, detail="User not c")
    return jwt_payload
