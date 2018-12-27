import unittest

import pytest

from batteries.oop.reflection.helpers import is_method as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsMethod(unittest.TestCase):

    def test_is_method_true_positives(self):
        self.assertTrue(uut(self.testcase, 'abstract_class_method'))
        self.assertTrue(uut(self.testcase, 'abstract_instance_method'))
        self.assertTrue(uut(self.testcase, 'abstract_static_method'))
        self.assertTrue(uut(self.testcase, 'class_method'))
        self.assertTrue(uut(self.testcase, 'instance_method'))
        self.assertTrue(uut(self.testcase, 'parent_class_method'))
        self.assertTrue(uut(self.testcase, 'parent_instance_method'))
        self.assertTrue(uut(self.testcase, 'parent_static_method'))
        self.assertTrue(uut(self.testcase, 'static_method'))

    def test_is_method_true_negatives(self):
        self.assertFalse(uut(self.testcase, '__abstract_private_decorated_property'))
        self.assertFalse(uut(self.testcase, '__abstract_private_method'))
        self.assertFalse(uut(self.testcase, '__parent_private_decorated_property'))
        self.assertFalse(uut(self.testcase, '__parent_private_instance_method'))
        self.assertFalse(uut(self.testcase, 'abstract_decorated_property'))
        self.assertFalse(uut(self.testcase, 'decorated_property'))
        self.assertFalse(uut(self.testcase, 'parent_decorated_property'))
