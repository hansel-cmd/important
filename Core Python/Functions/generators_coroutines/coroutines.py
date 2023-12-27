"""
Coroutines do not start on their own. They will execute/start when
u invoke __next__() or pass the obj to next(). Using decorator,
we can start coroutines without calling __next__() since the 
decorator will handle the starting for us
"""

def coroutine(function):
    def start(*args, **kwargs):
        result = function(*args, **kwargs)
        next(result)
        return result
    return start

@coroutine
def my_coroutine(x):
    print(f"Starting with {x}")
    b = yield x
    print(f"However I got sent a {b} and yielded {x}")
    c = x + b
    yield c
    print(f"I yielded back a {c} and exited")
    yield 'haha'

@coroutine
def get_this_number(number):
    try:
        while True:
            b = yield 
            if b == None:
                print("Please give me a number!")
            if b == number:
                return "SUCCESS"
    except GeneratorExit:
        print("I am closing now...")


x = get_this_number(10)
x.send('hahah') # without the decorator coroutine, this line will throw an error
x.close()
try:
    x.send(10) # it stops if it matches
except StopIteration as e:
    print(e)