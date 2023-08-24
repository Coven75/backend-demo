import uuid
from typing import Optional, Any

from bson import ObjectId
from pydantic import Field, BaseModel

from core.enum.language_enum import Language
from core.enum.mode_enum import Mode


class UserTenant(BaseModel):
    id: ObjectId = Field(alias="_id", default_factory=uuid.uuid4)
    name: str = Field(...)
    key: str = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserModel(BaseModel):
    id: ObjectId = Field(alias="_id")
    firstName: str = Field(...)
    lastName: str = Field(...)
    password: str = Field(...)
    language: Language = Field(default=Language.EN)
    email: str = Field(...)
    currentTenant: Optional[UserTenant] = Field(...)
    tenants: list[UserTenant] = Field(...)
    mode: Mode
    archived: bool = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
