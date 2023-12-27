class MyClass:
    class_attr = "Class Attribute"

    def __init__(self, a, b):
        self.a = a # instance attributes due to self
        self.b = b
        # creates an instance attribute hiding the class attribute
        self.class_attr = "Instance Attribute"

    def __call__(self): # callable
        print("Invoking myself...")

my_class = MyClass(1,2)
print(my_class.class_attr)


class MathUtils:
    @staticmethod
    def add(x, y):
        # static method since it is related to the class
        # but doesnt necessarily work with the attributes
        return x + y
    
print(MathUtils.add(1,2))


class ShippingContainer:

    next_serial = 600 # class attribute

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

    @classmethod
    def _generate_serial(cls):
        # class method since it works directly with
        # the class attribute, next_serial

        # if this was an ordinary method where we use self
        # instead of cls, each instance will have the same
        # serial number.
        next = cls.next_serial
        cls.next_serial += 1
        return next
    
    @staticmethod
    def get_shipping_type():
        return "General Shipping Container"
    

s1 = ShippingContainer('s1', ['GIRLS Album'])
print(s1.serial)
s2 = ShippingContainer('s2', ['SAVAGE Album'])
print(s2.serial)

print(ShippingContainer.get_shipping_type())

class RefrigeratedShippingContainer(ShippingContainer):
    pass

r1 = RefrigeratedShippingContainer('r1', ['fish'])
print(r1.get_shipping_type())
