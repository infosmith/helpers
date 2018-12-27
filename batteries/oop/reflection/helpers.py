"""Helper functions for reflection/inspecting objects."""
import inspect


def get_attributes(instance):
    return inspect.getmembers(instance)


def get_attribute_labels(instance):
    for attribute in inspect.getmembers(instance):
        yield attribute[0]


def has_attribute(instance, attribute):
    return hasattr(instance, attribute)


def is_callable(attribute, instance=None):
    """Check if value or attribute of instance are callable."""
    try:
        if instance:
            return callable(getattr(instance, attribute))
        else:
            return callable(attribute)
    except AttributeError:
        return False


def is_method(instance, attribute):
    """Check if attribute of instance exists and is callable."""
    return is_callable(attribute, instance=instance)


def is_magic(attribute):
    """Check if attribute name matches magic attribute convention."""
    return all([
        attribute.startswith('__'),
        attribute.endswith('__')])


def is_magic_method(instance, attribute):
    """Check if attribute is a magic method."""
    return all([
        is_magic(attribute),
        is_method(instance, attribute)])


def is_mangled(attribute):
    """Check if attribute has mangled name."""
    return any([
        is_mangled_name(attribute),
        is_mangled_name_attempt(attribute)])


def is_mangled_name(attribute):
    """Check if attribute conforms to name mangling convention."""
    return attribute.startswith('__') and not attribute.endswith('__')


def is_mangled_name_attempt(attribute):
    """Check if attribute attempts to conform to name mangling convention."""
    return all([
        attribute[0] == '_',
        attribute[1] != '_',
    ]) and not any([
        attribute.endswith('_'),
        attribute.endswith('__')])


def is_private(attribute):
    """Check if attribute is private by checking name mangling."""
    return is_mangled(attribute)


def is_private_method(instance, attribute):
    """Check if attribute is a privately scoped callable."""
    return all([
        has_attribute(instance, attribute),
        is_private(attribute),
        is_method(instance, attribute),
    ]) and not is_magic(attribute)


def is_property(instance, attribute):
    """Check if attribute is a property."""
    return all([
        has_attribute(instance, attribute),
    ]) and not any([
        is_method(instance, attribute),
        is_private_method(instance, attribute),
        is_magic(attribute)])


def is_public_method(instance, attribute):
    """Check if attribute is a publicly scoped callable."""
    return all([
        has_attribute(instance, attribute),
        is_method(instance, attribute),
    ]) and not any([
        is_private(attribute),
        is_magic(attribute)])


def is_public_property(instance, attribute):
    """Check if attribute is a publicly scoped property."""
    return all([
        has_attribute(instance, attribute),
        is_property(instance, attribute),
    ]) and not any([
        is_private(attribute),
        is_magic(attribute)])
