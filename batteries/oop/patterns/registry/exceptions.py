"""Exceptions of Registry Pattern Implementations."""


class RegistryException(Exception):
    pass


class RegistryKeyException(RegistryException, KeyError):
    pass
