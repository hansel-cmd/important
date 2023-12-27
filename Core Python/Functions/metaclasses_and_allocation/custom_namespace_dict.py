"""
We can create a custom namespace dictionary by overriding the return value
from the __prepare__ function of the metaclass.
"""

class OneShotNameSpace(dict):
    def __init__(self, name, existing=None):
        super().__init__()
        self._name = name
        if existing is not None:
            for k, v in existing.items():
                self.__setitem__(name, k, v)

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(
                f"Cannot reassign {key!r} of "
                f"class instance {self._name!r}"
            )
        super().__setitem__(key, value)

class ProhibitDuplicatesMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return OneShotNameSpace(name)


class Dodgy(metaclass=ProhibitDuplicatesMeta):

    def method(self):
        print("First Definition")

    def method(self):
        print("Second Definition")


dodgy = Dodgy()
dodgy.method()