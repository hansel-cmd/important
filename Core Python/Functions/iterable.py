"""Assumption: We have a perfect binary tree:
    That is, it contains 2^n - 1 levels.
"""

def is_perfect_length(sequence):
    n = len(sequence)
    power_of_2 = n + 1
    return (power_of_2 & n == 0) and n != 0

class LevelOrderIterator:

    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} "
                "does not represent a perfect binary tree "
                "with a length of 2^n - 1"
            )
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        item = self._sequence[self._index]
        self._index += 1
        return item


"""
(2 + 5) * (10 - 3)
"""
seq = LevelOrderIterator(['*', '+', '-', '2', '5', '10', '3'])
print(' '.join(seq))
# iterator = iter(seq)
# print(next(iterator))


def get_right_child(index):
    return 2 * index + 2

def get_left_child(index):
    return 2 * index + 1

class PreOrderIterator:

    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} "
                "does not represent a perfect binary tree "
                "with a length of 2^n - 1"
            )
        self._sequence = sequence
        self._stack = [0]

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stack:
            raise StopIteration
        
        current = self._stack.pop()

        # add the children to the stack
        right = get_right_child(current)
        left = get_left_child(current)

        if right < len(self._sequence):
            self._stack.append(right)
        
        if left < len(self._sequence):
            self._stack.append(left)

        return self._sequence[current]

    
seq1 = PreOrderIterator(['*', '+', '-', '2', '5', '10', '3'])
# * + 2 5 - 10 3
print(" ".join(seq1))


class InOrderIterator:

    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} "
                "does not represent a perfect binary tree "
                "with a length of 2^n - 1"
            )
        self._sequence = sequence
        self._stack = []
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self._stack) == 0 and self._index >= len(self._sequence):
            raise StopIteration
        
        # Push all left children of the index in question
        # into the stack until last leaf
        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = get_left_child(self._index)

        current_index = self._stack.pop()
        element = self._sequence[current_index]

        # Right children
        self._index = get_right_child(current_index)

        return element


seq2 = InOrderIterator(['*', '+', '-', '2', '5', '10', '3'])
print(" ".join(seq2))


missing = object()
seq3 = InOrderIterator(['+', 'r', '*', missing, missing, 'p', 'q'])

class SkipMissingIterator:

    def __init__(self, sequence, missing):
        # just get an iterator out of the sequence
        self._iterator = iter(sequence)
        self._missing = missing
    
    def __iter__(self):
        return self

    def __next__(self):
        # Loop the iterator using next() which
        # raises a StopIteration if it no longer
        # has a next element
        while True:
            element = next(self._iterator)
            if element is not self._missing:
                return element
            

skip = SkipMissingIterator(seq3, missing)
print(" ".join(skip))

# p * q - r / s + t
typesetting_table = {
    "-": "\u2212",
    "*": "\u00D7",
    "/": "\u00F7"
}

class TranslationIterator:
    def __init__(self, sequence, table = {
        "-": "\u2212",
        "*": "\u00D7",
        "/": "\u00F7"
    }):
        self._iterator = iter(sequence)
        self._table = table

    def __iter__(self):
        return self
    
    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)


seq4 = InOrderIterator(['-', '*', '/', 'p', 'q', 'r', '+', missing, missing, missing, missing, missing, missing, 's', 't'])
print(" ".join(TranslationIterator(SkipMissingIterator(seq4, missing))))