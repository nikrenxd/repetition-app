from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ALLOWED_HOSTS: str
    CSRF_TRUSTED_ORIGINS: str
    CORS_ALLOWED_ORIGINS: str
    DEBUG: int = Field(default=0)
    DJANGO_SECRET: str

    ACCESS_TOKEN_EXPIRES: int
    REFRESH_TOKEN_EXPIRES: int


config = Config()
