from bson import ObjectId
from pydantic import Field, BaseModel


class EntityModel(BaseModel):
    id: ObjectId = Field(alias="_id")
    name: str = str
    key: str = str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}



