from pydantic import BaseModel, Field, HttpUrl, EmailStr
import uuid

class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class UserSchema(BaseModel):
    id:str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")

class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Course Title"
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=50)
    description: str = "Course Description"
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")
    estimated_time: str = Field(alias="estimatedTime", default="6 weeks")

course_default_model = CourseSchema(
    id="course_001",
    title="Introduction to Python",
    maxScore=100,
    minScore=50,
    description="A beginner's course on Python programming.",
    previewFile=FileSchema(
        id="file_001",
        url="http://example.com/preview.pdf",
        filename="preview.pdf",
        directory="/files/preview"
    ),
    createdByUser=UserSchema(
        id="user_001",
        email="asd@example.com",
        firstName="John",
        lastName="Doe",
        middleName="A"
    ),
    estimatedTime="4 weeks"
)

print("Course Default Model:", course_default_model)

course_dict = {
    "id": "course_002",
    "title": "Advanced Python",
    "maxScore": 100,
    "minScore": 60,
    "description": "An advanced course on Python programming.",
    "previewFile": {
        "id": "file_002",
        "url": "http://example.com/advanced_preview.pdf",
        "filename": "advanced_preview.pdf",
        "directory": "/files/advanced_preview"
    },
    "createdByUser": {
        "id": "user_002",
        "email": "asd@example.com",
        "firstName": "Jane",
        "lastName": "Smith",
        "middleName": "B"
    },
    "estimatedTime": "6 weeks"
}

course_from_dict = CourseSchema(**course_dict)
print("Course from Dictionary:", course_from_dict)

course_json = """
{
    "id": "course_002",
    "title": "Advanced Python",
    "maxScore": 100,
    "minScore": 60,
    "description": "An advanced course on Python programming.",
    "previewFile": {
        "id": "file_002",
        "url": "http://example.com/advanced_preview.pdf",
        "filename": "advanced_preview.pdf",
        "directory": "/files/advanced_preview"
    },
    "createdByUser": {
        "id": "user_002",
        "email": "asd@example.com",
        "firstName": "Jane",
        "lastName": "Smith",
        "middleName": "B"
    },
    "estimatedTime": "6 weeks"
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("Course from JSON:", course_json_model)

