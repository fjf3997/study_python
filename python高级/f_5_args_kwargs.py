def test2(a, b, *args, **kwargs):
    print("-----------------")
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a, b, *args, **kwargs)


if __name__ == '__main__':
    test1(1, 2, 33, 44, 55, name="fjf", age=18)
