import os
import unittest

from helpers.elma.logs import Log


class TestGetAttributeLabels(unittest.TestCase):

    def setUp(self):
        self.log = Log('testing', path='.')

    def tearDown(self):
        os.remove(self.log.path)

    def test_path_attribute(self):
        assert self.log.path.endswith('.log')

    def test_path_attribute_unset(self):
        log = Log('unpersisted')
        assert log.path is None

    def test_log_file_handler_path_exists(self):
        assert os.path.exists(self.log.path)
