# def escape_letters(f):
#     def wrapper(*args, **kwargs):
#         print("Hello world")
#         x = f(*args, **kwargs)
#         return ascii(x)
#     return wrapper


# @escape_letters
# def say():
#     return "þink always!"


# print(say())


# Instances as Decorators
class Tracer:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrapper():
            if self.enabled:
                print("Tracing...")
            f()
        return wrapper


tracer = Tracer()

@tracer
def func():
    print("Hello World!")

# func()
# func()
# tracer.enabled = False
# func()
# func()
# func()


# # Classes as Decorators
class Logger:
    def __init__(self, f):
        self.enabled = True
        self.f = f

    def __call__(self):
        print("Logging...")
        self.f()
    
@Logger
@tracer
def func_2():
    "func2 is a Function 2."
    print("Welcome to my World!")

from functools import wraps

def greetings(f):
    @wraps(f)
    def wrapper():
        "A decorator wrapper called Greetings."
        print("Gomenesai")
        f()
    return wrapper


@greetings
def say_hi():
    "A function that says Hi in Korean"
    print("Annyeonhaseyo")

print(say_hi.__doc__)


def check_non_negative(param):
    def decorator(f):
        # wrapper will always get the parameters in the decorated funtion
        def wrapper(*args):
            if args[param] < 0:
                return
            return f(*args)
        return wrapper
    return decorator

# This is not a decorator itself. It is a function that returns the decorator.
# Parameterized Decorators
@check_non_negative(1)
def create_list(init, size):
    return [init] * size


print(create_list('a', -1))