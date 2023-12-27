from abc import ABCMeta, abstractmethod

"""
from collections.abc import Sized

class Test:
    pass
    
a = Test()
isinstance(a, Sized) -> False

Apparently, implementing a __len__() inside class Test, will
suffice it to be considered as a subclass of Sized ABC.

class Test:
    def __len__(self):
        // code here
    
a = Test()
isinstance(a, Sized) -> True

"""


class SwordMeta(type):

    def __subclasscheck__(cls, subclass):
        if (
            hasattr(subclass, "swipe") and callable(subclass.swipe)
            and
            hasattr(subclass, "sharpen") and callable(subclass.sharpen)
       
        ):
            return True
        return super().__subclasscheck__(subclass)
    
    def __instancecheck__(cls, subclass):
        return cls.__subclasscheck__(subclass)

"""

"""
class Sword(metaclass=SwordMeta):
    """Abstract Base Class"""
    
    def thrust(self):
        print("Thrust!", type(self).__name__)
    
"""
Although BroadSword is a virtual subclass of its
virtual base class, Sword, it cannot call the method
thrust() defined in the virtual base class since the
BroadSword's mro does not contain the Sword class.

broad_sword = BroadSword()
broad_sword.__mro__

For the BroadSword to invoke the thrust() method, it
has to inherit it by explicitly putting the Sword
base class as its base class, i.e.:

class BroadSword(Sword):
    // code here...
"""
class BroadSword:

    def swipe(self):
        print("Swipe!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)

class SamuraiSword:

    def  swipe(self):
        print("Slice!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)

class Sabre(Sword):
    pass

class Rifle:

    def fire(self):
        print("Bang!", type(self).__name__)



broad_sword = BroadSword()
samurai_sword = SamuraiSword()
sabre = Sabre()
sword = Sword()

print(type(broad_sword))
print(type(samurai_sword))

print(issubclass(SamuraiSword, Sword))
print(issubclass(BroadSword, Sword))

print(isinstance(samurai_sword, Sword))
print(isinstance(broad_sword, Sword))


broad_sword.swipe()
