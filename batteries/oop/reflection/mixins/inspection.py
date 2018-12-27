""""""
import inspect

from .abstract import AbstractReflectionMixin


class InspectionMixin(AbstractReflectionMixin):

    @property
    def attributes(self):
        for member in inspect.getmembers(self):
            yield member

    @property
    def methods(self):
        for method in inspect.getmembers(self, predicate=inspect.isfunction):
            yield method

    @property
    def properties(self):
        condition = lambda m: not any([
            inspect.isfunction(m),
            inspect.ismethod(m),
        ])
        for attribute in inspect.getmembers(self, predicate=condition):
            yield attribute

    @property
    def parents(self):
        return inspect.getmro(self)[1:-1]

    @property
    def private_methods(self):
        raise NotImplemented()

    @property
    def private_properties(self):
        raise NotImplemented()

    @property
    def public_methods(self):
        raise NotImplemented()

    @property
    def public_properties(self):
        raise NotImplemented()

    @property
    def inherited_methods(self):
        raise NotImplemented()

    @property
    def inherited_properties(self):
        raise NotImplemented()

    @property
    def inherited_private_methods(self):
        raise NotImplemented()

    @property
    def inherited_private_properties(self):
        raise NotImplemented()

    @property
    def inherited_public_methods(self):
        raise NotImplemented()

    @property
    def inherited_public_properties(self):
        raise NotImplemented()

