"""Pytest test fixtures."""
import pytest

from .fixtures.oop.reflection import ReflectionTestCase



class Log(object):
    info = print
    warning = print
    error = print


@pytest.fixture(scope='class')
def oop_reflection_testcase(request):
    """Example pytest fixture."""
    request.cls.testcase = ReflectionTestCase()

def logging(request):
    request.cls.log = Log()