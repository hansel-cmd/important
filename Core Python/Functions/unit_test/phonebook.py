import os

class Phonebook:

    def __init__(self, cache_directory):
        self.numbers = {}
        self.filename = os.path.join(cache_directory, 'names.txt')
        self.cache = open(self.filename, "r+")
        for line in self.cache.readlines():
            name, number = line.rstrip('\n').split(',')
            self.numbers[name] = number
        self.close()

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]
    
    def names(self):
        return set(self.numbers.keys())
    
    def close(self):
        self.cache.close()