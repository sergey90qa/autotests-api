from httpx import Response
from clients.api_client import APIClient

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client

from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, CreateExerciseRequestSchema, GetExerciseResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema

class ExercisesClient(APIClient):
    """ Клиент для работы с /api/v1/exercises"""
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: httpx. Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения одного упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Httpx Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))


    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод частичного обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Любые изменяемые поля.
        :return: Httpx. Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Httpx. Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """Возвращает список упражнений (распарсенный JSON)."""
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """Возвращает одно упражнение (распарсенный JSON)."""
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """Создаёт упражнение и возвращает его (распарсенный JSON)."""
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """Частично обновляет упражнение и возвращает результат (распарсенный JSON)."""
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)




def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Билдер авторизованного клиента ExercisesClient.

    :param user: Данные аутентификации пользователя (токены/учётка).
    :return: Готовый к использованию ExercisesClient с приватным HTTP-клиентом.
    """
    return ExercisesClient(client= get_private_http_client(user))