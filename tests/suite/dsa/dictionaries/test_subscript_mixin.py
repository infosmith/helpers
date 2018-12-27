import unittest

from helpers.dsa.dictionaries.mixins import Subscriptable


class UnitUnderTest(Subscriptable):
    pass


class TestSubscriptable(unittest.TestCase):

    def test_subscript_mixin(self):
        uut = UnitUnderTest()
        uut['subscript'] = True
        self.assertTrue(uut['subscript'])

    def test_subscript_mixin_kwargs(self):
        uut = UnitUnderTest(data={"subscript":True})
        self.assertTrue(uut['subscript'])
