import unittest

import pytest

from batteries.dsa.dictionaries.recursive import RecursiveDictionary


@pytest.mark.usefixtures('logging')
class TestRecursiveDictionary(unittest.TestCase):

    def test_recursive_dictionary_arbitrary_nesting(self):
        try:
            uut = RecursiveDictionary()
            uut['a']['b']['c']['d']['e']['f']['g']['h'] = 1
        except KeyError:
            self.log.error('Arbitrary nesting failed!')
            raise AssertionError('Arbitrary nesting failed!')
