import unittest

import pytest

from helpers.oop.reflection.helpers import is_callable as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsCallable(unittest.TestCase):

    def test_is_callable_with_function(self):
        self.assertTrue(uut(print))

    def test_is_callable_with_instance_method(self):
        self.assertTrue(uut('instance_method', instance=self.testcase))
