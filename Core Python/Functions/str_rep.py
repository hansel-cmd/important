def test(format_spec):
    x, y, z = format_spec.partition('.')
    print(x)
    print(y)
    print(z)

test('.2f')