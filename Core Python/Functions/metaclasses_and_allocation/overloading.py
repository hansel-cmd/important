import inspect
from weakref import WeakKeyDictionary

def _type_hint_matches(obj, hint):
    # only works with concrete types, not things like Optional
    return hint is inspect.Parameter.empty or isinstance(obj, hint)


def _signature_matches(sig: inspect.Signature,
                       bound_args: inspect.BoundArguments):
    # doesn't handle type hints on *args or **kwargs
    for name, arg in bound_args.arguments.items():
        param = sig.parameters[name]
        hint = param.annotation
        if not _type_hint_matches(arg, hint):
            return False
    return True


class BoundOverloadDispatcher:
    def __init__(self, instance, owner_cls, cls_attr, overload_methods):
        self.instance = instance
        self.owner_cls = owner_cls
        self.cls_attr = cls_attr
        self.overload_methods = overload_methods

    def best_match(self, *args, **kwargs):
        for sig, f in self.overload_methods.items():
            try:
                bound_args = sig.bind(self.instance, *args, **kwargs)
            except:
                pass
            else:
                bound_args.apply_defaults()
                if _signature_matches(sig, bound_args):
                    return f
                
        raise Exception
            
    
    def __call__(self, *args, **kwargs):
        try:
            f = self.best_match(*args, **kwargs)
        except Exception:
            pass
        else:
            return f(self.instance, *args, **kwargs)
        
        super_instance = super(self.owner_cls, self.instance)
        super_call = getattr(super_instance, self.cls_attr, None)
        if super_call is not None:
            return super_call(*args, **kwargs)
        


class OverloadDescriptor:

    def __init__(self, overloaded_list):
        print("AAAAAAAAAAAA", overloaded_list)
        self.overloaded_methods = {
            inspect.signature(f): f
            for f in overloaded_list
        }
    
    def __set_name__(self, owner, cls_attr):
        self.owner = owner
        self.cls_attr = cls_attr

    def __get__(self, instance, owner):
        print("GETTTING>>>>>> ", self.owner, instance, owner)

        if instance is None:
            return self
        
        return BoundOverloadDispatcher(instance, self.owner, self.cls_attr, self.overloaded_methods)
    
    def __set__(self, instance, value):
        self._instance_data[instance] = value


class OverloadList(list):
    pass


class OverloadDict(dict):

    def __setitem__(self, key, value):
        if not inspect.isfunction(value):
            super().__setitem__(key, value)
            return
    
        is_overloaded = getattr(value, '__is_overload', False)
        if not is_overloaded:
            super().__setitem__(key, value)
            return
        
        if key in self:
            current_methods = self[key]
            super().__setitem__(key, OverloadList(current_methods + [value]))
        else: 
            super().__setitem__(key, OverloadList([value]))
            

class MyClassMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return OverloadDict()

    def __new__(mcs, name, bases, namespace, **kwargs):
        
        print("HELLO WORLD")
        # print(namespace.items())

        overload_namespace = {}
        for key, value in namespace.items():
            if isinstance(value, OverloadList):
                overload_namespace[key] = OverloadDescriptor(value)
            else:
                overload_namespace[key] = value

        print(overload_namespace)
        obj = super().__new__(mcs, name, bases, overload_namespace)
        return obj


def overload(f):
    f.__is_overload = True
    return f

class MyClass(metaclass=MyClassMeta):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @overload
    def log(self, x : int):
        print(self.log, f"accepts x : {type(x)}")

    @overload
    def log(self, x : str):
        print(self.log, f"accepts x : {type(x)}")

    @overload
    def log(self, *args):
        print(self.log, f"accepts *args with length : {len(args)}")

    def say(self):
        print("say hello")



my_class = MyClass(1, 2, 3)
# my_class.log('2')
my_class.log(11)
