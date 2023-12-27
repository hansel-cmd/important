from collections.abc import MutableSequence

class ModTwoSequence(MutableSequence):

    def __init__(self, sequence):
        self._sequence = sequence

    def __delitem__(self, index):
        del self._sequence[index]

    def __getitem__(self, index):
        return self._sequence[index]

    def __len__(self):
        return len(self._sesquence)
    
    def __setitem__(self, index, value):
        self._sequence[index] = value

    def insert(self, index, value):
        self._sequence.insert(index, value)

    def __repr__(self):
        return f"{type(self).__name__}({self._sequence})"


x = ModTwoSequence((1, 2, 3, 4))
x.insert(0, 8)
print(x)