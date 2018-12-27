import unittest

import pytest

from helpers.oop.reflection.helpers import is_public_property as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsPublicProperty(unittest.TestCase):
    """Verify outcomes of is_public_property(obj, attribute) function."""

    def test_is_public_property_true_positives(self):
        self.assertTrue(uut(self.testcase, 'abstract_class_property'))
        self.assertTrue(uut(self.testcase, 'abstract_decorated_property'))
        self.assertTrue(uut(self.testcase, 'abstract_instance_property'))
        self.assertTrue(uut(self.testcase, 'class_property'))
        self.assertTrue(uut(self.testcase, 'decorated_property'))
        self.assertTrue(uut(self.testcase, 'instance_property'))
        self.assertTrue(uut(self.testcase, 'parent_class_property'))
        self.assertTrue(uut(self.testcase, 'parent_decorated_property'))
        self.assertTrue(uut(self.testcase, 'parent_instance_property'))

    def test_is_public_property_true_negatives(self):
        self.assertFalse(uut(self.testcase, '__dict__'))
        self.assertFalse(uut(self.testcase, '__init__'))
        self.assertFalse(uut(self.testcase, '__private_instance_method'))
        self.assertFalse(uut(self.testcase, '__private_decorated_property'))
        self.assertFalse(uut(self.testcase, '_private_instance_method'))
        self.assertFalse(uut(self.testcase, 'class_method'))
        self.assertFalse(uut(self.testcase, 'instance_method'))
        self.assertFalse(uut(self.testcase, 'static_method'))
