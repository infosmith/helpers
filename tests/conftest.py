"""Testing fixtures."""
import pytest


@pytest.fixture(scope='class')
def example_pytest_fixture(request):
    """Example pytest fixture."""
    request.cls.example_pytest_fixture = 4
