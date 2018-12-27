import unittest

from batteries.oop.reflection.helpers import is_mangled_name_attempt as uut


class TestIsMangledNameAttempt(unittest.TestCase):

    def test_is_mangled_name_attempt_true_positives(self):
        self.assertTrue(uut('_method'))

    def test_is_mangled_name_attempt_true_negatives(self):
        self.assertFalse(uut('__method'))
        self.assertFalse(uut('__method__'))
        self.assertFalse(uut('method'))
