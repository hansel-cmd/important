from abc import ABC, abstractmethod

class Sword(ABC):
    """Abstract Base Class"""

    """
    This check is for virtual relations, i.e.,
    virtual base class and virtual subclass
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return  (
            # duck type checks for virtual relations
            hasattr(subclass, "swipe") and callable(subclass.swipe)
            and
            hasattr(subclass, "parry") and callable(subclass.parry)
            and
            hasattr(subclass, "sharpen") and callable(subclass.sharpen)
            or
            NotImplemented # or via register
        )

    @abstractmethod
    def swipe(self):
        raise NotImplementedError
    
    @abstractmethod
    def sharpen(self):
        raise NotImplementedError
    
    @abstractmethod
    def parry(self):
        print("Parry!", type(self).__name__)
    
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
class BroadSword(Sword):

    def swipe(self):
        print("Swipe!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)

    def parry(self):
        super().parry()

"""
SamuraiSword is a virtual subclass of Sword base class.

Sword is a virtual base class of SamuraiSword.

For issubclass() and isinstance() to be true, this
virtual class has to implement all methods defined in its
virtual base class, Sword, and the base class, Sword,
must have a __subclasshook__ implemented.
"""
class SamuraiSword:

    def swipe(self):
        print("Slice!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)

    def parry(self):
        super().parry()

class Sabre:

    def swipe(self):
        print("Slice!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)

    def parry(self):
        super().parry()

"""
Subclass registration weakens the base class concept since
registration can bypapss interface detection.

ABCs are meant to be implemented via its abstract
methods.
"""
@Sword.register
class LightSabre:
    
    def swipe(self):
        print("Fffkkkrrrrzzzzzshhhh!", type(self).__name__)


@Sword.register
class KnifeToy:

    def swipe(self):
        print("Swing!", type(self).__name__)

class Rifle:

    def fire(self):
        print("Bang!", type(self).__name__)


def test_sub_class(this, of):
    print(f"{this.__name__} issubclass of {of.__name__} = "
          f"{issubclass(this, of)}")
    
def test_is_instance(this, of):
    print(f"{type(this).__name__} isinstance of {of.__name__} = "
          f"{isinstance(this, of)}")
    

broad_sword = BroadSword()
samurai_sword = SamuraiSword()
sabre = Sabre()

print(type(broad_sword))
print(type(samurai_sword))

test_sub_class(SamuraiSword, Sword)
test_sub_class(BroadSword, Sword)
test_sub_class(Sabre, Sword)

print()

test_is_instance(samurai_sword, Sword)
test_is_instance(broad_sword, Sword)
test_is_instance(sabre, Sword)


knife_toy = KnifeToy()
test_sub_class(KnifeToy, Sword)

light_sabre = LightSabre()
test_sub_class(LightSabre, Sword)

