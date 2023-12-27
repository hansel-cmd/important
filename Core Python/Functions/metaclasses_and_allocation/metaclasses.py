class ClassMetaTest(type):
    
    """
    name -> class name as a string
    bases  -> tuple of base classes associated with the class
    namespace -> mapping returned from __prepare__
    **kwargs -> keyword arguments
    """
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("ClassMetaTest.__prepare__(name, bases, **kwargs)")
        print(f"    {mcs=}")
        print(f"    {name=}")
        print(f"    {bases=}")
        print(f"    {kwargs=}")
        namespace = super().__prepare__(name, bases)
        print(f"-> {namespace = }")
        print()
        return namespace
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("ClassMetaTest.__new__(mcs, name, bases, namespace, **kwargs)")
        print(f"    {mcs=}")
        print(f"    {name=}")
        print(f"    {bases=}")
        print(f"    {namespace=}")
        print(f"    {kwargs=}")
        cls = super().__new__(mcs, name, bases, namespace)
        print(f"-> {cls = }")
        print()
        return cls
    
    def __init__(cls, name, bases, namespace, **kwargs):
        print("ClassMetaTest.__init__(cls, name, bases, namespace)")
        print(f"    {cls=}")
        print(f"    {name=}")
        print(f"    {bases=}")
        print(f"    {namespace=}")
        print(f"    {kwargs=}")
        super().__init__(name, bases, namespace)
        print()

    def metamethod(cls):
        print("ClassMetaTest.metamethod(cls)")
        print(f"    {cls=}")

    def __call__(cls, *args, **kwargs):
        print("ClassMetaTest.__call__(cls, *args, **kwargs)")
        print(f"    {cls=}")
        print(f"    {args=}")
        print(f"    {kwargs=}")
        obj = super().__call__(*args, **kwargs)
        print(f"-> {obj = }")
        print()


class Test(metaclass=ClassMetaTest):
    def __new__(cls, *args, **kwargs):
        print("Test.__new__(cls, *args, **kwargs)")
        print(f"    {cls=}")
        print(f"    {args=}")
        print(f"    {kwargs=}")
        obj = super().__new__(cls)
        print(f"-> {obj = }")
        print()

    def __init__(self, *args, **kwargs):
        print("Test.__init__(self, *args, **kwargs)")
        print(f"    {self=}")
        print(f"    {args=}")
        print(f"    {kwargs=}")
        print()


s = Test()
# print(type(Test))