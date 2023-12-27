class MyContextManager():

    def __enter__(self):
        print("You are in a with-block")
        return self
    
    def __exit__(self, type, value, traceback):
        print("Logging MyContextManager.__exit__")
        if type is None:
           print("Normal Exit detected")
           return True
        print("Exception is detected")
        raise
        
        
        
try:
    with MyContextManager() as x:
        # print(x)
        raise ValueError()
except ValueError as e:
    print("Exception caught", e)

print()

import contextlib

@contextlib.contextmanager
def cm():
    try:
        print("__enter__")
        yield '-----You are in a with-block'
        print("__exit__ normally")
    except:
        print("__exit__ with exception")


# with cm() as c:
#     raise ValueError()