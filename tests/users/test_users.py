from http import HTTPStatus
import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from clients.users.public_users_client import PublicUsersClient
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake

@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    @pytest.mark.parametrize("domain", [
        "mail.ru",
        "gmail.com",
        "example.com"
    ])
    def test_create_user(self, public_users_client: PublicUsersClient, domain: str):
        email = fake.email(domain)
        request = CreateUserRequestSchema(email=email)
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user_me(self, private_users_client: PrivateUsersClient, function_user: UserFixture):
        response = private_users_client.get_user_me_api()
        assert_status_code(response.status_code, HTTPStatus.OK)

        get_user_response = GetUserResponseSchema.model_validate_json(response.text)
        get_user_response_user = get_user_response.user
        create_user_response_user = function_user.response.user

        assert_get_user_response(get_user_response_user, create_user_response_user)
        validate_json_schema(response.json(), get_user_response.model_json_schema())

