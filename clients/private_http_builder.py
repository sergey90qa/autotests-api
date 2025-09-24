from httpx import Client
from pydantic import BaseModel, EmailStr
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from functools import  lru_cache

class AuthenticationUserSchema(BaseModel, frozen = True):
    email: str
    password: str

@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)
    """
    Функция для получения клиента HTTP, который будет использоваться для приватных запросов.

    :return: Экземпляр httpx.Client с базовым URL и таймаутами.
    """
    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers= {"Authorization": f"Bearer {login_response.token.access_token}"}
    )

