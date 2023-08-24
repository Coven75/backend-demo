from pydantic import BaseModel


class SignInApi(BaseModel):
    email: str
    password: str
