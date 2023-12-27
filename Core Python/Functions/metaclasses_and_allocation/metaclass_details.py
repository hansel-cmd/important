class EntriesMeta(type):

    def __new__(mcs, name, bases, namespaces, **kwargs):
        print("EntriesMeta.__new_(mcs, name, bases, namespaces, **kwargs)")
        print(f"    {kwargs=}")
        num_entries = kwargs['num_entries']
        print(f"    {num_entries}")
        namespaces.update({
            chr(i): i for i in range(ord('a') + num_entries)
        })
        return super().__new__(mcs, name, bases, namespaces)
    

class AtoZ(metaclass=EntriesMeta, num_entries=26):
    pass


atoz = AtoZ()