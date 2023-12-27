from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    # first_name : str
    # last_name : str

    def __init__(self, first_name : str, last_name : str):
        self.first_name = first_name
        self.last_name = last_name
        # super().__init__()

    def __repr__(self):
        return f"{type(self).__name__}: {self.first_name} {self.last_name}" + \
                f" hash = {hash(self)}"
    
    def __hash__(self):
        return hash((self.first_name, self.last_name))
        
    def __eq__(self, others):
        if not isinstance(self, type(others)):
            return NotImplemented

        return (
            self.first_name == others.first_name and \
            self.last_name == others.last_name
        )

    # def __setattr__(self, name, value):
    #     print(name, value, self.__dict__)
    #     if name in self.__dict__:
    #         raise AttributeError(
    #             f"Cannot reassign attribute {name} of "
    #             f"type {type(self).__name__}"
    #             )
    #     self.__dict__[name] = value
        


p = Person('Katarina', 'Yu')
p2 = Person('Winter', 'Kim')

d = {}
d[p] = 100
d[p2] = 200
print(d)
print(d[p])

p.first_name = 'KARINA'
# print(d)
# print(d[p])