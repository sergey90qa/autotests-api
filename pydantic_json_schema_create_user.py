from clients.users.public_users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),,
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
print(create_user_response)
print(create_user_response_schema)

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)