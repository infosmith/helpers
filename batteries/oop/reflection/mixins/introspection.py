from .abstract import AbstractReflectionMixin
from batteries.oop import (
    is_private_method,
    is_public_property,
    is_public_method,
)


class IntrospectionMixin(AbstractReflectionMixin):

    @property
    def attributes(self):
        for attribute in dir(self):
            yield attribute

    @property
    def inherits(self):
        for parent in self.parents:
            for attribute in dir(parent):
                yield attribute

    @property
    def methods(self):
        for attribute in self.attributes:
            if is_public_method(self, attribute):
                yield attribute

    @property
    def parents(self):
        for parent in self.__class__.__mro__[1:-1]:
            yield parent

    @property
    def private_methods(self):
        for attribute in self.attributes:
            if is_private_method(self, attribute):
                yield attribute

    @property
    def properties(self):
        for attribute, value in self.attributes:
            if is_public_property(self, attribute):
                yield attribute, value
