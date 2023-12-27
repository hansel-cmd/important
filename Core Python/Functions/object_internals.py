class Vector:

    def __init__(self, **args):
        private_components = {
            f"_{k}": v
            for k, v in args.items()
        }
        self.__dict__.update(private_components)

    # executes when accessing an non-existent attribute.
    # In other words, executes when lookup of __getattribute__ fails.
    # Must directly check whether the attribute exists in __dict__
    def __getattr__(self, name):
        private_name = f"_{name}"
        if private_name not in self.__dict__:
            raise AttributeError(f"{self!r} has no attribute {name!r}")
        return getattr(self, private_name)
            
    def __setattr__(self, name, _):
        raise AttributeError(f"Cannot set attribute {name!r}")
    
    def __delattr__(self, name):
        raise AttributeError(f"Cannot delete attribute {name!r}")

    def __repr__(self):
        args_list = self._get_args()
        return "{typename}({args})".format(
            typename = type(self).__name__,
            args = ", ".join(
                "{} = {}".format(k, v) for k,v in args_list.items()
            )
        )
    
    def _get_args(self):
        return {k[1:]:v for k, v in self.__dict__.items()}
    

class ColoredVector(Vector):

    def __init__(self, red, green, blue, **components):
        super().__init__(**components)
        self.__dict__['_colors'] = {
            "red": red,
            "green": green,
            "blue": blue
        }

    def _get_args(self):
        super_args = super()._get_args()
        super_args.update({
            k : v for k, v in super_args['colors'].items()
        })
        del super_args['colors']
        return super_args
    


v = Vector(p = 5, x = 10, w  = 20)
print(v.a)
# delattr(v, 'p')


cv = ColoredVector(red=255,green=96,blue=34, a = 10, b = 24)
# print(cv)