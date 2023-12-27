def fibonacci(n):
    if n < 0:
        raise ValueError("Incorrect input {n}")
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonacci(n - 1) + fibonacci(n - 2)
    
def fibonacci_optimized(n):
    a = 1
    b = 2
    if n < 0:
        raise ValueError("Incorrect input {n}")
    if n == 1:
        return a
    if n == 2:
        return b
    
    for _ in range (2, n):
        c = a + b
        a = b
        b = c
    return b

"==========================================================="

class FibonacciIterable:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{type(self).__name__}({self.start}, {self.end})"
    
    def __iter__(self):
        return FibonacciIterator(self.start, self.end)
    
class FibonacciIterator:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0

    def __next__(self):
        if self.start + self.increment > self.end:
            raise StopIteration
        fibonacci_number = fibonacci(self.start + self.increment)
        self.increment += 1
        return fibonacci_number

    def __iter__(self):
        return self
    
"==========================================================="

class FibonacciGenerator:

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"{type(self).__name__}({self.start}, {self.end})"
    
    def __iter__(self):
        for i in range(self.start, self.end):
            yield fibonacci(i)

"==========================================================="

class FibonacciGeneratorOptimized:

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"{type(self).__name__}({self.start}, {self.end})"
    
    def __iter__(self):
        for i in range(self.start, self.end):
            yield fibonacci_optimized(i)

"==========================================================="

class FibonacciGeneratorLazyOptimized:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.fibonacci_dict = {
            x : fibonacci(x)
            for x in range(start, end)
        }

    def __repr__(self):
        return f"{type(self).__name__}({self.start}, {self.end})"
    
    def __iter__(self):
        for key in self.fibonacci_dict:
            yield self.fibonacci_dict[key]

"==========================================================="

class FibonacciIterableLazyOptimized:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{type(self).__name__}({self.start}, {self.end})"

    def __iter__(self):
        return FibonacciIteratorLazyOptimized(self.start, self.end)
    
class FibonacciIteratorLazyOptimized:
     
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.fibonacci_dict = {
            x : fibonacci_optimized(x)
            for x in range(start, end + 1)
        }
        self.increment = 0

    def __next__(self):
        if self.start + self.increment > self.end:
            raise StopIteration
        fibonacci_number = self.fibonacci_dict[self.start + self.increment]
        self.increment += 1
        return fibonacci_number
    
    def __iter__(self):
        return self
    

class Call:
    
    def __init__(self, it, start, end):
        self.it = it
        self.start =  start
        self.end = end

    def __call__(self, *args, **kwargs):
        for _ in self.it(self.start, self.end):
            pass

if __name__ == "__main__":
    import timeit
    import numpy as np
    start = 2
    end = 20

    fibonacci_iterable = FibonacciIterable
    fibonacci_generator = FibonacciGenerator
    fibonacci_generator_optimized = FibonacciGeneratorOptimized
    fibonacci_generator_lazy_optimized = FibonacciGeneratorLazyOptimized
    fibonacci_iterable_lazy_optimized = FibonacciIterableLazyOptimized

    for iterable in [
                fibonacci_iterable, 
                fibonacci_generator,
                fibonacci_generator_optimized,
                fibonacci_generator_lazy_optimized,
                fibonacci_iterable_lazy_optimized
            ]:
        print(f"For the iterable {iterable} we got \n")
        print(
            f"""{np.mean(
                timeit.repeat(
                    Call(iterable, start, end),
                    number = 5,
                    repeat = 5
                )):0.5f}""", '\n'
        )