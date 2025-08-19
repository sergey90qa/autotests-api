from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.publick_http_builder import get_public_http_client

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str | None

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа при создании пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request:CreateUserRequestDict) -> Response:
        """
        Метод для создания нового пользователя.

        :param request: Словарь с данными пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request:CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Метод для создания нового пользователя и получения данных о нём.

        :param request: Словарь с данными пользователя.
        :return: Данные о созданном пользователе в виде словаря.
        """
        response = self.create_user_api(request)
        return response.json()

def get_public_user_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client= get_public_http_client())