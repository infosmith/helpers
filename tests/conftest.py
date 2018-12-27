"""Pytest test fixtures."""
import pytest

from .fixtures.oop.reflection import ReflectionTestCase



class Log(object):
    info = print
    warning = print
    error = print


@pytest.fixture(scope='class')
def logging(request):
    request.cls.log = Log()

@pytest.fixture(scope='class')
def oop_reflection_testcase(request):
    request.cls.testcase = ReflectionTestCase()
