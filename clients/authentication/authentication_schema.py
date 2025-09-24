from pydantic import BaseModel, Field, EmailStr
from tools.fakers import fake


class TokenSchema(BaseModel):
    """Описание структуры аутентификационных токенов"""
    access_token: str = Field(alias="accessToken")
    token_type: str = Field(alias="tokenType")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """Описание структуры запроса на аутентификацию"""
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class LoginResponseSchema(BaseModel):
    """Описание структуры ответа на аутентификацию"""
    token: TokenSchema

class RefreshTokenRequestSchema(BaseModel):
    """Описание структуры запроса на обновление токена"""
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)