from typing import List, Dict

from core.model.common_query_params import CommonQueryParams
from core.model.context_data import ContextData
from database.database import database
from models.tenant.user_profile_model import UserProfileModel


def get_user_profile_repository():
    return UserProfileRepository().instance()


class UserProfileRepository:
    _instance = None
    collection_name: str = "userProfile"

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def get_user_profile_list(self, commons: CommonQueryParams, context_data: ContextData) -> List[UserProfileModel]:
        return (database.get_tenant_collection(context_data.currentTenant, self.collection_name)
                .find({})
                .skip(commons.pageIndex * commons.pageSize)
                .limit(commons.pageSize))

    def count_user_profile(self, context_data: ContextData) -> int:
        return database.get_tenant_collection(context_data.currentTenant, self.collection_name).count_documents({})

    def get_user_profile_by_id(self, user_profile_id: str, context_data: ContextData) -> UserProfileModel:
        return (database.get_tenant_collection(context_data.currentTenant, self.collection_name)
                .find_one({"_id": user_profile_id}))
