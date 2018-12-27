from batteries.oop.patterns.registry import Registry


registry = Registry()


class RegistryTestEntry(object):

    def to_upper(self, msg):
        return msg.upper()


@registry.register_class('class-a')
class A(RegistryTestEntry):
    pass


@registry.register_class('class-b')
class B(RegistryTestEntry):
    pass


@registry.register_class('class-c')
class C(RegistryTestEntry):
    pass


@registry.register_class('class-d')
class D(RegistryTestEntry):
    pass
