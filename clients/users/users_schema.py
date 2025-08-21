from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании пользователя.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: str | None
    password: str | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа для обновления пользователя.
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema