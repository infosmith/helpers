import random
import unittest
from array import array
from collections import (
    defaultdict, namedtuple, OrderedDict, Counter
)
from datetime import (
    date, datetime, time, timezone
)
from enum import Enum

from helpers.elma.exceptions import raise_if_not_type

types = [
    array,
    complex,
    Counter,
    date,
    datetime,
    defaultdict,
    dict,
    Enum,
    float,
    frozenset,
    int,
    list,
    namedtuple,
    None,
    OrderedDict,
    set,
    str,
    time,
    timezone,
    tuple,
]

instances = [1, 2.0, [], {}, None, defaultdict(int), range(10)]


def filter_if_in(iter, excludes):
    return [e for e in iter if not e in excludes]


class TestRaiseIfNotType(unittest.TestCase):

    def test_raise_if_not_type(self):
        given = random.choice(instances)
        exclude = given.__class__
        with self.assertRaises(ValueError):
            raise_if_not_type(given, filter_if_in(types, excludes=[exclude]))
