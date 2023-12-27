def squared(iterable):
    return (i ** 2 for i in iterable)


def negate(iterable):
    return (-i for i in iterable)

def add_one(iterable):
    return (i + 1 for i in iterable)

def pipeline(iterable):
    return add_one(
        negate(
            squared(iterable)
        )
    )

print(pipeline([1,2,3,4,5]))
print(list(pipeline([1,2,3,4,5])))
