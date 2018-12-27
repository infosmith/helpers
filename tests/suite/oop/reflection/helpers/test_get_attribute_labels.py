import unittest

import pytest

from helpers.oop.reflection.helpers import get_attribute_labels


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestGetAttributeLabels(unittest.TestCase):

    def test_get_attribute_labels(self):
        outcome = sorted(get_attribute_labels(self.testcase))
        expected = sorted(dir(self.testcase))
        self.assertEqual(outcome, expected)
