import unittest

import pytest

from helpers.oop.reflection.helpers import is_magic_method as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsMagicMethod(unittest.TestCase):

    def test_is_magic_method_true_positives(self):
        self.assertTrue(uut(self.testcase, '__getattribute__'))
        self.assertTrue(uut(self.testcase, '__init__'))
        self.assertTrue(uut(self.testcase, '__new__'))
        self.assertTrue(uut(self.testcase, '__setattr__'))

    def test_is_magic_method_true_negatives(self):
        self.assertFalse(uut(self.testcase, '__abstract_private_decorated_property'))
        self.assertFalse(uut(self.testcase, '__abstract_private_instance_method'))
        self.assertFalse(uut(self.testcase, '__parent_private_decorated_property'))
        self.assertFalse(uut(self.testcase, '__parent_private_instance_method'))
        self.assertFalse(uut(self.testcase, '__private_decorated_property'))
        self.assertFalse(uut(self.testcase, '__private_instance_method'))
        self.assertFalse(uut(self.testcase, '_abstract_private_instance_method'))
        self.assertFalse(uut(self.testcase, '_parent_private_instance_method'))
        self.assertFalse(uut(self.testcase, '_private_instance_method'))
        self.assertFalse(uut(self.testcase, 'abstract_class_method'))
        self.assertFalse(uut(self.testcase, 'abstract_decorated_property'))
        self.assertFalse(uut(self.testcase, 'abstract_instance_method'))
        self.assertFalse(uut(self.testcase, 'abstract_static_method'))
        self.assertFalse(uut(self.testcase, 'class_method'))
        self.assertFalse(uut(self.testcase, 'decorated_property'))
        self.assertFalse(uut(self.testcase, 'instance_method'))
        self.assertFalse(uut(self.testcase, 'parent_class_method'))
        self.assertFalse(uut(self.testcase, 'parent_decorated_property'))
        self.assertFalse(uut(self.testcase, 'parent_instance_method'))
        self.assertFalse(uut(self.testcase, 'parent_static_method'))
        self.assertFalse(uut(self.testcase, 'static_method'))

    def test_is_magic_method_possible_confusion(self):
        self.assertFalse(uut(self.testcase, '__dict__'))
        self.assertFalse(uut(self.testcase, '__getattr__'))
        self.assertFalse(uut(self.testcase, '__getitem__'))
        self.assertFalse(uut(self.testcase, '__setitem__'))
