"""
Interning should only be used for immutable value types.
"""
# With Interning
class ChessCoordinate1:

    _interned = {}

    def __new__(cls, file, rank):

        if file not in 'abcdefgh':
           raise ValueError(f"{file} is out of range")
       
        if rank not in range(1,9):
           raise ValueError(f"{rank} is out of range")
       
        obj = object.__new__(cls)
        key = (file, rank)
        if key not in cls._interned:
            cls._interned[key] = obj
            obj._file = file
            obj._rank = rank

        return cls._interned[key]

    def __init__(self, file, rank):
       pass
      

    @property
    def file(self):
        return self._file
    
    @property
    def rank(self):
        return self._rank
    
    def __str__(self):
        return f"{self._file}{self._rank}"


# Without Interning
class ChessCoordinate:

    def __new__(cls, *args, **kwargs):

        obj = object.__new__(cls)
        # print(f"args = {args!r}")
        # print(f"kwargs = {kwargs!r}")
        # print(f"id(obj) = {id(obj)}")
        return obj

    def __init__(self, file, rank):
       
    #    print(f"id(self) = {id(self)}")
       
       if file not in 'abcdefgh':
           raise ValueError(f"{file} is out of range")
       
       if rank not in range(1,9):
           raise ValueError(f"{rank} is out of range")
       
       self._file = file
       self._rank = rank

    @property
    def file(self):
        return self._file
    
    @property
    def rank(self):
        return self._rank
    
    def __str__(self):
        return f"{self._file}{self._rank}"


def test_memory_usage(cls, info):
    import tracemalloc

    tracemalloc.start()
    boards = [cls('a', 4) for _ in range(10000)]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_kb = peak / 1000

    print(f"{info} {peak_kb:.0f} kB")

# Without Interning
test_memory_usage(ChessCoordinate, "w/o interning:")

# With Interning    
test_memory_usage(ChessCoordinate1, "w/ interning:")

