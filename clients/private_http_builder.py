from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict
from typing import TypedDict

class AuthenticationUserDict(TypedDict):
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserDict) -> Client:
    authentication_client = get_authentication_client()
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)
    """
    Функция для получения клиента HTTP, который будет использоваться для приватных запросов.

    :return: Экземпляр httpx.Client с базовым URL и таймаутами.
    """
    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers= {f"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )