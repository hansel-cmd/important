from collections.abc import Iterable

def flatten(iterables):
    
    for iterable in iterables:
        if isinstance(iterable, Iterable):
            yield from flatten(iterable)
        else:
            yield iterable


sample = [
    [1, 2, 3, 4, 5, 6, 7,],
    8,
    (9, 10, 11, 12, 13),
    [
        [14, 15, 16, 17,],
        [18, [19, 20, 21], 22],
        23
    ],
    ([24, 25, (26, 27)], 28)
]
print(list(flatten(sample)))