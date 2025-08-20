from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")

user = User(id= 1, name="Alice", address=Address(city="Moscow", zip_code="111111"), email="alice@example.com")
print(user)