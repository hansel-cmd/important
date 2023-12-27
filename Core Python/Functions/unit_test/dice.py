"""
execute: python -m doctest <filename>.py -v
"""


def get_total(dice):
    """
    Sums all the given dice.

    >>> get_total([1,2,3,4,5])
    15

    >>> get_total([1,2,3,5,4])
    0

    It doesn't accept unsorted list

    >>> get_total([5, 4, 3, 2, 1])
    0
    """

    if all(dice[i] < dice[i + 1] for i in range(len(dice) - 1)):
        return sum(dice)

    return 0

class X:
    def method(self):
        return 'hello world'

def test():
    """
    Test doctest with output that varies, i.e., object references, etc.

    >>> test() #doctest: +ELLIPSIS
    <bound method X.method of <dice.X object at 0x...>>
    """
    x = X()
    return x.method


def traceback():
    """
    This function raises ValueError regardless.

    >>> traceback()
    Traceback (most recent call last):
    ...
    ValueError: Test Error :)
    """
    raise ValueError("Test Error :)")
