import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")

@pytest.fixture(scope= 'session')
def settings():
    print("[SESSION] Инициализируем настройки авто тестов")

@pytest.fixture(scope= "class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope= "function")
def users_client(settings):
    print("[FUNCTION] Создаем api client на каждый авто тест")

class TestUserFlow:
    def test_user_can_login(self, user, users_client):
        ...

    def test_user_can_create_course(self, user, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self, user, users_client):
        ...

@pytest.fixture(scope="function")
def user_data() -> dict:
    yield {"username": "test_user", "email": "test@example.com"}

def test_user_email(user_data: dict):
    assert user_data["email"] == "test@example.com"

def test_user_name(user_data: dict):
    assert user_data["username"] == "test_user"