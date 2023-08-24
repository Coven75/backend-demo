from typing import List

from database.database import database
from models.core.user_model import UserModel


def get_user_repository():
    return UserRepository().instance()


class UserRepository:
    _instance = None
    collection_name: str = "user"

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def get_user_profile_list(self) -> List[UserModel]:
        return (database.get_collection(self.collection_name)
                .find({}))

