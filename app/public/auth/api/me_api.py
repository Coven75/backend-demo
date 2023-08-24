from typing import Optional

from pydantic import BaseModel

from core.enum.mode_enum import Mode
from models.core.tenant_model import TenantModel
from models.core.user_model import UserModel, UserTenant


class TenantApi(BaseModel):
    id: str
    name: str
    key: str

    @classmethod
    def to_api(cls, tenant: UserTenant):
        return cls(
            id=str(tenant.id),
            name=tenant.name,
            key=tenant.key
        )


class MeApi(BaseModel):
    id: str
    email: str
    firstName: str
    lastName: str
    tenants: list[TenantApi]
    currentTenant: Optional[TenantApi]
    mode: Mode

    @classmethod
    def to_api(cls, user: UserModel):
        return cls(
            id=str(user.id),
            email=user.email,
            firstName=user.firstName,
            lastName=user.lastName,
            mode=user.mode,
            tenants=[TenantApi.to_api(tenant) for tenant in user.tenants],
            currentTenant=TenantApi.to_api(user.currentTenant) if user.currentTenant else None
        )
