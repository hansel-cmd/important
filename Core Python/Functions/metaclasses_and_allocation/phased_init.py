class PhasedMeta(type):

    def __call__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._pre_init(*args, **kwargs)
        obj.__init__(*args, **kwargs)
        obj._post_init(*args, **kwargs)

class PhasedInit(metaclass=PhasedMeta):

    def __init__(self):
        print("Initialization...")

    def _pre_init(self):
        print("Pre-Initialization...")
    
    def _post_init(self):
        print("Post-Initialization...")

class SubPhasedInit(PhasedInit):

    def __init__(self):
        super().__init__()
        print("Sub-Initialization...")


p = SubPhasedInit()
print(p)