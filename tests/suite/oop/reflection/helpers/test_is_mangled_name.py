import unittest

from batteries.oop.reflection.helpers import is_mangled_name as uut


class TestIsMangledName(unittest.TestCase):

    def test_is_mangled_name_true_positives(self):
        self.assertTrue(uut('__method'))

    def test_is_mangled_name_true_negatives(self):
        self.assertFalse(uut('__magical__'))
        self.assertFalse(uut('method'))
        self.assertFalse(uut('_method'))
