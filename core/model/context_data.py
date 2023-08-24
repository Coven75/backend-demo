from typing import Any

from pydantic import BaseModel

from models.core.tenant_model import TenantModel
from models.core.user_model import UserModel


class ContextData(BaseModel):
    user: UserModel
    currentTenant: TenantModel
