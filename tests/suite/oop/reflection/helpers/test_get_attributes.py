import unittest

import pytest

from batteries.oop.reflection.helpers import get_attributes as uut


@pytest.mark.usefixtures('oop_reflection_testcase')
class TestGetAttributes(unittest.TestCase):

    def test_get_attributes(self):
        for label, value in uut(self.testcase):
            self.assertIn(label, dir(self.testcase))
