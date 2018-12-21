"""Tests for `batteries` package."""
import unittest

import pytest



@pytest.mark.usefixtures('example_pytest_fixture')
class TestBatteries(unittest.TestCase):
    """Tests for `batteries` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.example_setup_fixture = 4


    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass


    def test_with_pytest_fixture(self):
        """"""
        self.assertEqual(2 + 2, self.example_pytest_fixture)


    def test_with_setup_fixture(self):
        self.assertEqual(2 + 2, self.example_setup_fixture)
