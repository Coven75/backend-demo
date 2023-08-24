from bson import ObjectId
from pydantic import Field, BaseModel


class UserEmbedded:
    id: ObjectId = Field(alias="_id")
    firstName: str = str
    lastName: str = str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class EntityEmbedded:
    id: ObjectId = Field(alias="_id")
    name: str = str
    key: str = str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserProfileModel(BaseModel):
    id: ObjectId = Field(alias="_id")
    user: UserEmbedded = Field(...)
    entity: EntityEmbedded = Field(...)
    admin: bool = bool

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
