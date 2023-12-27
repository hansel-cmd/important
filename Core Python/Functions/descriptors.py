"""
Apparently, we can make use of the @property decorator 
and its @<property_name>.setter to make a "private" attribute.

This implementation is using descriptors, where prior @decorators
are not yet available in the Python environment.

Example:
a private '_name' attribute can be bound by a descriptor using the following:

name = property(
    fget=_get_name,
    fset=_set_name
)

def _get_name(self): return self._name
def _set_name(self, value): self._name = value

property function will return a descriptor where fget= and fset= are
assigned to its getters and setters functions.


--------
Non-data Descriptors only implement __get__. Thus, read-only.
Data Descriptors implement __get__, __set__, __delete__. Thus, writeable.

"""

from weakref import WeakKeyDictionary

"""
This will be a custom descriptor class.
"""
class Positive:
    """A data-descriptor for positive numeric values."""
    def __init__(self):
        self._instance_data = WeakKeyDictionary()

    def __set_name__(self, owner, cls_attr):
        print("AHAHAHAHA", owner, cls_attr)
        self._name = cls_attr

    """
        args: 
            self - descriptor object
            instance - instance from which the descriptor is retrieved
            owner - class to which the descriptor is bound

        When invoked from the descriptor object, it is similiar to:
        Positive.__get__(
            Planet.__dict__['<property_name>'], 
            pluto, # -> This is the instance object.
            Planet
        )

    """
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # print(self._instance_data.__dict__)
        return self._instance_data[instance]
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self._name} {value} is not positive")
        self._instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError(f"Cannot delete {self._name} attribute.")


class Planet:

    def __init__(self, name, radius_metres, mass_kilograms, 
                 orbital_period_seconds, surface_temperature_kelvin):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    def _get_name(self):
        return self._name
    
    def _set_name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name
    )
    
    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()

pluto = Planet(name='Pluto', 
               radius_metres=1184e3, 
               mass_kilograms=1.305e22, 
               orbital_period_seconds=7816012992, 
               surface_temperature_kelvin=55)

mars = Planet(name='Mars', 
               radius_metres=2222e3, 
               mass_kilograms=1.445e22, 
               orbital_period_seconds=44444444, 
               surface_temperature_kelvin=552)

pluto.radius_metres = 20
pluto.surface_temperature_kelvin = 201

print(pluto.radius_metres)
print(pluto.surface_temperature_kelvin)
print(mars.surface_temperature_kelvin)
# print(Planet.__dict__['radius_metres'])
print(Planet.radius_metres)