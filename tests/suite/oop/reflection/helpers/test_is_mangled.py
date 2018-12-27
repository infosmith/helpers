import unittest

from batteries.oop.reflection.helpers import is_mangled as uut


class TestIsMangled(unittest.TestCase):

    def test_is_mangled_true_positives(self):
        self.assertTrue(uut('__method'))
        self.assertTrue(uut('_method'))

    def test_is_mangled_true_negatives(self):
        self.assertFalse(uut('__magical__'))
        self.assertFalse(uut('method'))
