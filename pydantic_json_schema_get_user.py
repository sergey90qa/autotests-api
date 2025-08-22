from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

create_public_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    lastName ="string",
    firstName ="string",
    middleName ="string"
)

public_user_client = get_public_user_client()
create_public_user_response = public_user_client.create_user(create_public_user_request)

authentication_user_request = AuthenticationUserSchema(
    email=create_public_user_request.email,
    password=create_public_user_request.password
)

private_user_client = get_private_users_client(authentication_user_request)
get_user_response = private_user_client.get_user_api(create_public_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

