def set_fun(fun):
    print("--------装饰器一--------")

    def add_func(*args, **kwargs):
        print("-----功能一--------")
        return  fun(*args, **kwargs)
    return add_func


def add_fun(fun):
    print("-----------装饰器二---------")

    def add_func(*args, **kwargs):
        print("-----功能二--------")
        return  fun(*args, **kwargs)
    return add_func



@set_fun
@add_fun
def test():
    print("-----test-------")


test()
