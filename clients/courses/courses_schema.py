from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema

class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    minScore: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    createdByUser: UserSchema

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании курса.
    """
    course: CourseSchema

class CoursesQueryParamsSchema(BaseModel):
    """
    Описание структуры параметров запроса для получения курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str | None = Field(alias="userId")

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None =Field(alias="minScore")
    description: str | None
    estimated_time: str | None =Field(alias="estimatedTime")