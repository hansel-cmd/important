class SimpleList:
    def __init__(self, items):
        self._items = items
        print('SimpleList.__init__')
    
    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}(items = {self._items})'


class SortedList(SimpleList):
    def __init__(self, items=[]):
        super().__init__(items)
        print("SortedList.__init__")
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

class IntList(SimpleList):
    def __init__(self, items=[]):
        for item in items:
            self._validate(item)
        super().__init__(items)
        print("InitList.__init__")
    
    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only accepts integer values.')
        
    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    def __init__(self, items=[]):
        super().__init__(items)


# print(issubclass(SortedIntList, SimpleList))
# sil = SortedIntList([4,3,2,1])
# print(sil)

print(SortedIntList.__mro__)
sil = SortedIntList([4,1,3,2])