import unittest

import pytest

from helpers.oop.reflection.helpers import is_property as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsProperty(unittest.TestCase):

    def test_is_property_true_positive_cases(self):
        self.assertTrue(uut(self.testcase, 'class_property'))
        self.assertTrue(uut(self.testcase, 'decorated_property'))

    def test_is_property_true_negative_cases(self):
        self.assertFalse(uut(self.testcase, '__str__'))
        self.assertFalse(uut(self.testcase, 'non_existent'))
        self.assertFalse(uut(self.testcase, 'instance_method'))
