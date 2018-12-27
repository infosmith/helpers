"""Registry Design Pattern."""
from .exceptions import RegistryKeyException


class Registry(dict):

    def __init__(self, name=None, includes=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        for registry in includes:
            if registry.name:
                self[registry.name] = registry
            else:
                self.update(registry)

    def __getitem__(self, key):
        """Retrieve item from registry using sub-script notation."""
        try:
            return self[key]
        except KeyError:
            raise RegistryKeyException("{} is not registered".format(key))


    def register_class(self, key):
        """Decorator for registering classes."""

        def register_class_wrapper(cls):
            self[key] = cls
            return cls

        return register_class_wrapper
