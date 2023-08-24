from typing import List

from fastapi import Depends

from core.model.common_query_params import CommonQueryParams
from core.model.context_data import ContextData
from database.database import database
from models.core.user_model import UserModel
from repositories.user_profile_repository import get_user_profile_repository, UserProfileRepository
from repositories.user_repository import get_user_repository


def get_admin_user_service():
    return AdminUserService().instance()


class AdminUserService:
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.user_profile_repo = get_user_profile_repository()
        self.user_repo = get_user_repository()

    def get_user_list(self, commons: CommonQueryParams, context_data: ContextData) -> List[UserModel]:
        users_profiles_cursor = database.get_tenant_collection(context_data.currentTenant, "userProfile").find({}).skip(
            commons.pageIndex * commons.pageSize).limit(commons.pageSize)
        toto = self.user_profile_repo.get_user_profile_list(commons, context_data)
        print(toto)
        users_profiles: List[UserModel] = list(users_profiles_cursor)
        count = database.get_tenant_collection(context_data.currentTenant, "userProfile").count_documents({})

        return []
