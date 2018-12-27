"""Super-class of reflection mix-ins.

Defines reflection interface based on taxonomy
extracted from the Python object model.


Presumes
========
- Attribute describe any name following dot notation [1]
- Attribute references are the only operations instance objects understand [*1]
- Two kinds of valid attribute names: data attributes and methods [1]
- No universally accepted terminology of classes [1]
- Object-oriented semantics closest to Modula-3, not C++ or Small Talk [1]


References
==========
1. https://docs.python.org/3/tutorial/classes.html

- https://docs.python.org/3/library/abc.html
"""
from abc import ABC, abstractmethod


class AbstractReflectionMixin(ABC):

    @property
    @abstractmethod
    def attributes(self):
        """Return data attributes AND methods."""
        raise NotImplemented()

    @property
    @abstractmethod
    def inherited_methods(self):
        """Return inherited public AND private methods."""
        raise NotImplemented()

    @property
    @abstractmethod
    def inherited_properties(self):
        """Return inherited public AND private data attributes."""
        raise NotImplemented()

    @property
    @abstractmethod
    def inherited_private_methods(self):
        """Return inherited private methods."""
        raise NotImplemented()

    @property
    @abstractmethod
    def inherited_private_properties(self):
        """Return inherited private data attributes."""
        raise NotImplemented()

    @property
    @abstractmethod
    def methods(self):
        """Return method methods a.k.a. behaviors."""
        raise NotImplemented()

    @property
    @abstractmethod
    def parents(self):
        """Return parent classes in MRO."""
        raise NotImplemented()

    @property
    @abstractmethod
    def private_methods(self):
        """Return private methods."""
        raise NotImplemented()

    @property
    @abstractmethod
    def private_properties(self):
        """Return private data attributes."""
        raise NotImplemented()

    @property
    @abstractmethod
    def properties(self):
        """Return data attributes a.k.a. properties, variables."""
        raise NotImplemented()
