from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос создания упражнения.
    """
    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос обновления упражнения.
    """
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос получения списка упражнений.
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос получения упражнения.
    """
    exercise: ExerciseSchema

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры параметров запроса для получения упражнений.
    """
    course_id: str | None = Field(alias="courseId")

class CreateExerciseRequestSchema(BaseModel):
    """ Описание структуры запроса на создание упражнения."""
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseRequestSchema(BaseModel):
    """ Описание структуры запроса на обновление упражнения."""
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")