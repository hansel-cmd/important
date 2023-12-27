import inspect
from functools import wraps

def postcondition(predicate):

    def the_decorator(f):

        @wraps(f)
        def wrapper(self, *args, **kwargs):
            # wrapper always receives the arguments of the
            # decorated function
            # may or may not return something
            result = f(self, *args, **kwargs)
            if not predicate(self._locations):
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not "
                    f"maintained for {self!r}"
                )
            return result

        return wrapper
        
    return the_decorator

def at_least_two_locations(locations):
    return len(locations) > 1

def no_duplicate(locations):
    seen_locations = []
    for location in locations:
        if location.name in seen_locations:
            return False
        seen_locations.append(location.name)
    return True

# class decorator factory
def invariant(predicate):
    # becomes the decorator itself
    function_decorator = postcondition(predicate)

    # the decorator to be returned. It accepts the class itself
    def class_decorator(cls):

        members = list(vars(cls).items())
        for name, member in members:
            # if the member is a function, decorate it with
            # the decorator returned by postcondition
            if inspect.isfunction(member):
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)

        # should always return the class 
        return cls
    
    return class_decorator

def auto_repr(cls):
    print(f"Decorating {cls.__name__} with auto repr")
    members = vars(cls)
    # for name, member in members.items():
    #     print(name, member)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")
    
    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")
    
    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    # print("__init__ parameter names: ", parameter_names)

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all "
            "__init__ parameters have matching properties"
        )
    
    def synthesized_repr(self):
        args_list = []
        for name in parameter_names:
            args_list.append(
                "{name} = {value}".format(name = name, value = getattr(self, name))
            )
                                        
        return "{typename}({args})".format(typename = type(self).__name__, 
                                           args = ", ".join(args_list))

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class EarthPosition:

    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude
    
    @property
    def longitude(self):
        return self._longitude

    # def __repr__(self):
    #     return f"{type(self).__name__}(latitude = {self._latitude}, longitude = {self._longitude})"


@auto_repr
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position
    
    # def __repr__(self):
    #     return f"{type(self).__name__}(name = {self._name}, position = {self._position})"
    
    def __str__(self):
        return self._name


hk = Location("Hong Kong", EarthPosition(22.29, 114.16))
print(repr(hk))

sk = EarthPosition(29.32, 441.23)
print(repr(sk))
print()
print()

@invariant(no_duplicate)
@invariant(at_least_two_locations)
class Itinerary:

    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)
    
    # we uncomment this decorator since we will use
    # a class decorator factory. Refer to the decorator
    # of this class.
    # @postcondition(at_least_two_locations)
    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self._locations)
    
    def __len__(self):
        return len(self._locations)
    
    @property
    def locations(self):
        return tuple(self._locations)
    
    @property
    def origin(self):
        return self._locations[0]
    
    @property
    def destination(self):
        return self._locations[-1]
    
    # @postcondition(at_least_two_locations)
    def add(self, location):
        self._locations.append(location)

    # @postcondition(at_least_two_locations)
    def remove(self, name):
        self._locations = [
            location
            for _, location in enumerate(self._locations)
            if location.name != name
        ]

    # @postcondition(at_least_two_locations)
    def truncate_at(self, name):
        index = None
        for ndx, location in enumerate(self._locations):
            if location.name == name:
                index = ndx
                break

        self._locations = self._locations[0:index + 1]

    
itinerary = Itinerary.from_locations(
    Location(name = 'Hong Kong', position = EarthPosition(latitude = 123, longitude = 34)),
    Location(name = 'Singapore', position = EarthPosition(latitude = 44, longitude = 23)),
    Location(name = 'South Korea', position = EarthPosition(latitude = 16, longitude = 1155)),
    Location(name = 'Japan', position = EarthPosition(latitude = 32, longitude = 22)),
    Location(name = 'Malaysia', position = EarthPosition(latitude = 94.2, longitude = 22.8)),
)

itinerary.remove('Hong Kong')
# print(itinerary.origin)

# itinerary.truncate_at('Singapore')
# print(itinerary)