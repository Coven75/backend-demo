from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    PORT: int
    DB_NAME: str
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_EXPIRES: str
    JWT_ALGORITHM: str
    DEBUG_MODE: bool = True
    COOKIE_NAME: str = "SESSION"

    class Config:
        env_file = ".env"


settings = Settings()
