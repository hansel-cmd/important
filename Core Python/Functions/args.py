def test(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

test('Hello', 'World', 'Karina', 'Winter')

print("------------")

test_args = ("Welcome", "To", "My", "World")
test(*test_args)


def test2(arg1, arg2, a, savage):
    print(arg1)
    print(arg2)
    print(a)

test2("I", "am", **{"a": "a", "savage": "savage"})