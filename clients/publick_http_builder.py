from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция для получения клиента HTTP, который будет использоваться для публичных запросов.

    :return: Экземпляр httpx.Client с базовым URL и таймаутами.
    """
    return Client(timeout=100, base_url="http://localhost:8000")