import pytest
import sys

@pytest.mark.skip(reason="Фича в разработке")
def pytest_future_in_development():
    ...