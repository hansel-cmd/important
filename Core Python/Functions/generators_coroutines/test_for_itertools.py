"""
Given a list, we print the average up to a point.
x = [1, 2, 3]
average of first 1 element = 1
average of first 2 elements = 1.5
average of first 3 elements = 3

we return [1, 1.5, 3]
"""
import timeit

def old_school_averager(iterable):
    total = 0
    length = 0
    average = []
    for item in iterable:
        total += item
        length += 1
        average.append(total / length)
    return average


def old_school_averager_2(iterable):
    total = 0
    length = 0
    for item in iterable:
        total += item
        length += 1
        yield total / length

"""My Solution"""
def averager(iterable):
    return (
        sum(iterable[0 : index + 1]) / len(iterable[0 : index + 1]) 
        for index in range(len(iterable))
    )

import itertools

def averager_2(iterable):
    # return (
    #     total / (index + 1)
    #     for index, total in enumerate(itertools.accumulate(iterable))
    # )

    return itertools.starmap(
        lambda index, value: value / (index + 1),
        enumerate(itertools.accumulate(iterable))
    )


sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
# print(old_school_averager_2(sample))
print(list(averager_2(sample)))

print(timeit.timeit(
    stmt='old_school_averager(sample)',
    setup='from __main__ import old_school_averager, sample',
    number = 1000
))

print(timeit.timeit(
    stmt='list(old_school_averager_2(sample))',
    setup='from __main__ import old_school_averager_2, sample',
    number = 1000
))

print(timeit.timeit(
    stmt='list(averager_2(sample))',
    setup='from __main__ import averager_2, sample, itertools',
    number = 1000
))


print(timeit.timeit(
    stmt='list(averager(sample))',
    setup='from __main__ import averager, sample',
    number = 1000
))