import unittest

from tests.fixtures.oop.patterns.registry import registry


class TestRegistryPattern(unittest.TestCase):

    def setUp(self):
        self.registry = registry

    def test_registration_of_classes(self):
        for case in ['class-' + c for c in 'abcd']:
            self.assertTrue(case in self.registry)
