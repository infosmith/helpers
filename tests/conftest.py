"""Testing fixtures."""
import pytest

from .fixtures.oop.reflection import ReflectionTestCase



@pytest.fixture(scope='class')
def oop_reflection_testcase(request):
    """Example pytest fixture."""
    request.cls.testcase = ReflectionTestCase()
