class Test:

    def __init__(self, name, value):
        self.__dict__['_name'] = name
        self.__dict__['_value'] = value
    
    @property
    def value(self):
        return self._value
    
    @property
    def name(self):
        return self._name

    def __setattr__(self, name, value):
        private_component = f"_{name}"
        if private_component not in self.__dict__:
            raise AttributeError(f"Cannot set property {name}")
        self.__dict__[private_component] = value
        
    def __getattr__(self, name):
        print('ehllo')
        private_component = f"_{name}"
        if private_component not in self.__dict__:
            raise AttributeError(f"Attribute {name} is not present")
        return self.__dict__[private_component]


x = Test('Karina', 20)
# print(x.test)


from functools import reduce
my_list  = [1,2,3,4,5]

def add(i, j):
    return i + j

print(reduce(add, my_list, 0))
