from httpx import Response

from clients.api_client import APIClient

from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос создания упражнения.
    """
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос обновления упражнения.
    """
    exercise: Exercise

class GetExercisesResponse(TypedDict):
    """
    Описание структуры ответа на запрос получения списка упражнений.
    """
    exercises: list[Exercise]

class GetExerciseResponse(TypedDict):
    """
    Описание структуры ответа на запрос получения упражнения.
    """
    exercise: Exercise

class ExercisesQueryParams(TypedDict):
    """
    Описание структуры параметров запроса для получения упражнений.
    """
    courseId: str | None

class CreateExerciseRequestDict(TypedDict):
    """ Описание структуры запроса на создание упражнения."""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """ Описание структуры запроса на обновление упражнения."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """ Клиент для работы с /api/v1/exercises"""
    def get_exercises_api(self, query: ExercisesQueryParams) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения одного упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def post_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)


    def patch_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод частичного обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Любые изменяемые поля.
        :return: httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: ExercisesQueryParams) -> GetExercisesResponse:
        """Возвращает список упражнений (распарсенный JSON)."""
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponse:
        """Возвращает одно упражнение (распарсенный JSON)."""
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """Создаёт упражнение и возвращает его (распарсенный JSON)."""
        response = self.post_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """Частично обновляет упражнение и возвращает результат (распарсенный JSON)."""
        response = self.patch_exercise_api(exercise_id, request)
        return response.json()




def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Билдер авторизованного клиента ExercisesClient.

    :param user: Данные аутентификации пользователя (токены/учётка).
    :return: Готовый к использованию ExercisesClient с приватным HTTP-клиентом.
    """
    return ExercisesClient(client= get_private_http_client(user))