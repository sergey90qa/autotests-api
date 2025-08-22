from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema

class PrivateUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""
    def get_user_me_api(self) -> Response:
        """
        Получает информацию о текущем пользователе.
        :return:
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Получает информацию о пользователе по его ID.

        :param user_id: ID пользователя.
        :return: Ответ от сервера в виде объекта httpx. Response
        """
        return self.get(f"/api/v1/users/{user_id}")


    def update_user_api(self, user_id: int, request: UpdateUserRequestSchema) -> Response:
        """
        Обновляет информацию о пользователе по его ID.
        :param user_id:
        :param request:
        :return: Ответ от сервера в виде объекта httpx. Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: int) -> Response:
        """
        Удаляет пользователя по его ID.

        :param user_id: ID пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id:str) -> GetUserResponseSchema:
        """
        Получает информацию о пользователе по его ID.

        :param user_id: ID пользователя.
        :return: Данные о пользователе в виде словаря.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))