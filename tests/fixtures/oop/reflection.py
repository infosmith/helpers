import abc


class AbstractTestCase(abc.ABC):
    """Third element of Method Resolution Order."""
    abstract_class_property = 'abstract class property'

    def __init__(self, abstract_instance_property='abstract instance property value'):
        self.abstract_instance_property = abstract_instance_property

    @property
    def __abstract_private_decorated_property(self):
        return 'abstract private decorated property'

    def __abstract_private_instance_method(self):
        return 'abstract private method'

    def _abstract_private_instance_method(self):
        return 'abstract private instance method'

    @classmethod
    def abstract_class_method(cls):
        return  'abstract class method'

    @property
    def abstract_decorated_property(self):
        return 'abstract decorated property'

    def abstract_instance_method(self):
        return 'abstract method'

    @staticmethod
    def abstract_static_method():
        return 'abstract static method'


class ParentTestCase(AbstractTestCase):
    """Second element of Method Resolution Order"""
    parent_class_property = 'parent class property'

    def __init__(self, parent_instance_property='parent instance property value'):
        super().__init__()
        self.parent_instance_property = parent_instance_property

    @property
    def __parent_private_decorated_property(self):
        return 'parent private decorated property'

    def __parent_private_instance_method(self):
        return 'parent private method'

    def _parent_private_instance_method(self):
        return 'parent private instance method'

    @classmethod
    def parent_class_method(cls):
        return 'parent class method'

    @property
    def parent_decorated_property(self):
        return 'parent decorated property'

    def parent_instance_method(self):
        return 'parent instance method'

    @staticmethod
    def parent_static_method():
        return 'parent static method'


class ReflectionTestCase(ParentTestCase):
    """First element of Method Resolution Order"""
    class_property = 'class property'

    def __init__(self, instance_property='instance property value'):
        super().__init__()
        self.instance_property = instance_property

    @property
    def __private_decorated_property(self):
        return 'private decorated property'

    def __private_instance_method(self):
        return 'private instance method'

    def _private_instance_method(self):
        return 'private instance method'

    @classmethod
    def class_method(cls):
        return  'class method'

    @property
    def decorated_property(self):
        return 'decorated property'

    def instance_method(self):
        return 'instance method'

    @staticmethod
    def static_method():
        return 'static method'
