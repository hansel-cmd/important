import math

class InclinationError(Exception):
    pass

class TriangleError(Exception):
    
    def __init__(self, text, sides):
        super().__init__(text)
        self._text = text
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides
    
    @property
    def text(self):
        return self._text

    def __str__(self):
        return f"{self._text} for sides {self._sides}"
    
    def __repr__(self):
        return f"{type(self).__name__}({self._text}, {self._sides})"

# Heron's Formula
def triangle_area(a, b, c):
    sides = sorted([a, b, c])
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)

    p = (a + b + c) / 2
    result = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return result


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        # explicit chaining with the 'from e', and it associates
        # the chained exception to the __cause__
        raise InclinationError("Slope cannot be vertical") from e


def modulus_four(n):
    result = n % 4

    if result == 0:
        print("Multiple of 4")
    elif result == 1:
        print("Remainder of 1")
    elif result == 2:
        print("Remainder of 2")
    elif result == 3:
        print("Remainder of 3")
    else:
        # using assert will help figure out if 
        # the programmer has made a mistake in
        # the implementation
        assert False, "This should never be executed"


if __name__ == "__main__":

    # implicit chaining associates the chained exception
    # to the __context__
    try:
        area = triangle_area(14, 2, 3)
    except TriangleError as e:
        try:
            print(e, int('hello'))
        except ValueError as t:
            print(e)
            print(t)
            print(t.__context__ is e)

    print("---------------------------")
    print(inclination(0, 5))
    print("---------------------------")

    modulus_four(8)
