"""Mixin for adding subscript dictionary access."""


class Subscriptable(object):
    """Add subscript dictionary access."""

    def __init__(self, data={}):
        self.data = data

    def __contains__(self, item):
        return item in self.data

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        for key, value in self.data.items():
            yield key, value

    def __setitem__(self, key, value):
        self.data[key] = value
