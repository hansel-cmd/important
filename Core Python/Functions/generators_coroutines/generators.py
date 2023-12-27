class MyBombIterator:

    def __init__(self, count):
        self.count = count

    def __next__(self):
        if self.count <= 0:
            print("BOOOM!")
            raise StopIteration
        value =  self.count
        self.count -= 1
        return value

class MyBomb:

    def __init__(self, start):
        print(f"Activating the bomb and it will "
              f"expolde in {start} seconds")
        self.start = start

    def __iter__(self):
        # return MyBombIterator(self.start)
        return self

    def __next__(self):
        c = next(self)
        yield c
    
# bomb = MyBomb(5)
# bomb_iterator = iter(bomb)
# print(next(bomb_iterator))
# bomb_iterator = iter(bomb)
# print(next(bomb_iterator))
# print(next(bomb_iterator))
# print(next(bomb_iterator))
# print(next(bomb_iterator))
# print(next(bomb_iterator))
# print(next(bomb_iterator))


def generator_bomb(start):
    print(f"Activating bomb in {start} seconds")
    while start > 0:
        yield start
        start -= 1
    print("BOOM!")
    raise StopIteration

# b = generator_bomb(5)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

class MyNotLazySequenceIterator:
    
    def __init__(self, number):
        self.number = number
        self.sequence = {x: x ** 2 for x in range(number)}
        self.index = 0

    def __next__(self):
        try:
            value = self.sequence[self.index]
        except KeyError:
            raise StopIteration
        
        self.index += 1
        return value

class MyNotLazySequence:

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyNotLazySequenceIterator(self.number)
    
my_not_lazy_bomb = MyNotLazySequence(5)
my_not_lazy_bomb_iterator = iter(my_not_lazy_bomb)
print(next(my_not_lazy_bomb_iterator))
print(next(my_not_lazy_bomb_iterator))
print(next(my_not_lazy_bomb_iterator))
print(next(my_not_lazy_bomb_iterator))
print(next(my_not_lazy_bomb_iterator))
    
