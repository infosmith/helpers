import unittest

from helpers.oop.reflection.helpers import is_magic as uut


class TestIsMagic(unittest.TestCase):

    def test_is_magic_true_positives(self):
        self.assertTrue(uut('__dict__'))
        self.assertTrue(uut('__getattr__'))
        self.assertTrue(uut('__getattribute__'))
        self.assertTrue(uut('__getitem__'))
        self.assertTrue(uut('__init__'))
        self.assertTrue(uut('__new__'))
        self.assertTrue(uut('__setattr__'))
        self.assertTrue(uut('__setitem__'))

    def test_is_magic_true_negatives(self):
        self.assertFalse(uut('__abstract_private_decorated_property'))
        self.assertFalse(uut('__abstract_private_instance_method'))
        self.assertFalse(uut('__parent_private_decorated_property'))
        self.assertFalse(uut('__parent_private_instance_method'))
        self.assertFalse(uut('__private_decorated_property'))
        self.assertFalse(uut('__private_instance_method'))
        self.assertFalse(uut('_abstract_private_instance_method'))
        self.assertFalse(uut('_parent_private_instance_method'))
        self.assertFalse(uut('_private_instance_method'))
        self.assertFalse(uut('abstract_class_method'))
        self.assertFalse(uut('abstract_decorated_property'))
        self.assertFalse(uut('abstract_instance_method'))
        self.assertFalse(uut('abstract_static_method'))
        self.assertFalse(uut('parent_class_method'))
        self.assertFalse(uut('parent_decorated_property'))
        self.assertFalse(uut('parent_instance_method'))
        self.assertFalse(uut('parent_static_method'))
        self.assertFalse(uut('class_method'))
        self.assertFalse(uut('decorated_property'))
        self.assertFalse(uut('instance_method'))
        self.assertFalse(uut('static_method'))
