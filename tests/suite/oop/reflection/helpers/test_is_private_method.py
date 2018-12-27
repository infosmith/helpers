import unittest

import pytest

from batteries.oop.reflection.helpers import is_private_method as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsPrivateMethod(unittest.TestCase):

    def test_is_private_method_true_positive_cases(self):
        self.assertTrue(uut(self.testcase, '_private_instance_method'))

    def test_uut_true_negative_cases(self):
        self.assertFalse(uut(self.testcase, '__init__'))
        self.assertFalse(uut(self.testcase, 'instance_method'))
