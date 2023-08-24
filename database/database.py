import logging

from pymongo import MongoClient

from config import settings
from models.core.tenant_model import TenantModel


class DatabaseProvider:
    def __init__(self, ):
        self.client = MongoClient(settings.DB_URL)
        self.db = self.client.get_database("core")
        logging.info('Connected to MongoDB')

    def get_collection(self, collection_name: str):
        return self.__get_database__().get_collection(collection_name)

    def get_tenant_collection(self, tenant: TenantModel, collection_name: str):
        return self.__get_tenant_database__(tenant.key).get_collection(collection_name)

    def __get_database__(self):
        return self.db

    def __get_tenant_database__(self, tenant_key: str):
        return self.client.get_database("tenant_" + tenant_key)


database = DatabaseProvider()
