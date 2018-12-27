import unittest

import pytest

from helpers.oop.reflection.helpers import is_private as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestIsPrivate(unittest.TestCase):

    def test_is_private_true_positive_cases(self):
        self.assertTrue(uut('__method'))
        self.assertTrue(uut('_method'))

    def test_is_private_true_negative_cases(self):
        self.assertFalse(uut('__magical__'))
        self.assertFalse(uut('method'))
