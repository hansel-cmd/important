from dataclasses import dataclass

@dataclass
class Shape:
    sides: int
    name: str

    # runs after initializing instance variables
    # best to use to check variables' values
    def __post_init__(self):
        if self.sides < 0:
            raise ValueError("Shape requires a positive number of sides")
        if self.name == "":
            raise ValueError("Shape's name cannot be empty")

class Shape1:
    def __init__(self, sides, name):
        self._sides = sides
        self._name = name
    
    @property
    def sides(self):
        return self._sides

    @property
    def name(self):
        return self._name
    
    def __eq__(self, rhs):
        return self._sides == rhs._sides and \
                self._name == rhs._name


square = Shape1(4, 'square')
square1 = Shape1(4, 'square')
print(square == square1)


triangle = Shape(3, 'triangle')
triangle1 = Shape(3, 'triangle')
print(triangle == triangle1)

circle = Shape(0, "circle")
print(circle)