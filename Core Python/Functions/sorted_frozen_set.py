from collections.abc import Set

class SortedFrozenSet(Set):
    def __init__(self, items = None):
        self._items = sorted(
                set(items) if items is not None else set()
        )
        self._index = 0

    def __contains__(self, item):
        return item in self._items
    
    def __len__(self):
        return len(self._items)
    
    # if we just return self, we need to implement
    # __next__(). If we return an iterable, i.e.,
    # return iter(self._items), we dont need to implement
    # __next__().
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        
        item = self._items[self._index]
        self._index += 1
        
        return item
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return SortedFrozenSet(self._items[index])
        return self._items[index]
    
    def __repr__(self):
        arg = repr(self._items) if self._items else ""
        return (
            "{typename}({args})".format(
                typename = type(self).__name__,
                args = arg
            )
        )
    
    def __eq__(self, rhs):
        # This will allow Python to reverse (fallback) the order of
        # the operation where rhs will become lhs and will
        # raise a TypeError if fallback fails
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return self._items == rhs._items
    
    # Implement only if the obj is immutable
    # Since SortedFrozenSet is immutable but it
    # revolves around a mutable list object,
    # we have to make it a tuple as it is immutable
    def __hash__(self):
        # easiest way to implement a hash is to
        # hash a tuple with the type and its value
        return hash(
            (type(self), tuple(self._items))
        )
    
    # if __len__() and __getitem__() are both
    # implemented, we do not need to implement
    # __reversed__() as it will fallback to the 
    # two dunder methods.
    def __reversed__(self):
        # To be simpler, we can just do
        # return reversed(self._items), as reversed()
        # will return an iterable.
        r = self._items[::-1]
        return iter(r)

    def __add__(self, rhs):
        # This will allow Python to reverse (fallback) the order of
        # the operation where rhs will become lhs and will
        # raise a TypeError if fallback fails
        if not isinstance(rhs, type(self)):
            return NotImplemented
        
        return SortedFrozenSet(self._items + rhs._items)
    
    def __mul__(self, multiply):
        if multiply <= 0:
            return SortedFrozenSet([])
        return SortedFrozenSet(self._items)
    
    def __rmul__(self, multiply):
        # will run the __mul__()
        return self * multiply
    
    # We can skip this implementation by inheritance.
    # Just make this class inherit the
    # collections.abc.Sequence 
    def index(self, item):
        for ndx, value in enumerate(self._items):
            if value == item:
                return ndx
        raise ValueError
            
    # We can also skip this implementation by inheritance.
    # Just make this class inherit the
    # collections.abc.Sequence 
    def count(self, item):
        count = 0
        for i in self._items:
            if i == item: 
                count += 1
        return count
    
    def intersection(self, rhs):
        return self & SortedFrozenSet(rhs)

    def union(self, rhs):
        return self | SortedFrozenSet(rhs)
    
    def symmetric_difference(self, rhs):
        return self ^ SortedFrozenSet(rhs)

    def difference(self, rhs):
        return self - SortedFrozenSet(rhs)
    
    def issuperset(self, rhs):
        return self >= SortedFrozenSet(rhs)

    def issubset(self, rhs):
        return self <= SortedFrozenSet(rhs)

