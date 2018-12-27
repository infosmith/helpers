import unittest

import pytest

from helpers.oop.reflection.helpers import is_public_method as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsPublicMethod(unittest.TestCase):

    def test_is_public_method_true_positive_cases(self):
        self.assertTrue(uut(self.testcase, 'instance_method'))
        self.assertTrue(uut(self.testcase, 'static_method'))
        self.assertTrue(uut(self.testcase, 'class_method'))

    def test_is_public_method_true_negative_cases(self):
        self.assertFalse(uut(self.testcase, '_private_instance_method'))
        self.assertFalse(uut(self.testcase, '__private_instance_method'))
        self.assertFalse(uut(self.testcase, '__privated_decorated_property'))
        self.assertFalse(uut(self.testcase, 'decorated_property'))
        self.assertFalse(uut(self.testcase, '__init__'))
