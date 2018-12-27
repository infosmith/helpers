"""Pytest test fixtures."""
import pytest


class Log(object):
    info = print
    warning = print
    error = print


@pytest.fixture(scope='class')
def logging(request):
    request.cls.log = Log()
