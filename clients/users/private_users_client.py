from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления пользователя.
    """
    email: str | None
    password: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""
    def get_user_me_api(self) -> Response:
        """
        Получает информацию о текущем пользователе.
        :return:
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: int) -> Response:
        """
        Получает информацию о пользователе по его ID.

        :param user_id: ID пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: int, request: dict) -> Response:
        """
        Обновляет информацию о пользователе по его ID.
        :param user_id:
        :param request:
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: int) -> Response:
        """
        Удаляет пользователя по его ID.

        :param user_id: ID пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")