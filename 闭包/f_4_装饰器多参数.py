def add_fun(fun):
    def add_func(*args, **kwargs):
        print("-----功能一--------")
        print("-----功能二--------")
        return  fun(*args, **kwargs)
    return add_func


@add_fun
def test(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
    return "ok"


if __name__ == '__main__':

    ret = test(100, 200, 300, mm=100)
    print(ret)
