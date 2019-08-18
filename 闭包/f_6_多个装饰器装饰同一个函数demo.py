def set_fun(fun):
    def add_func(*args, **kwargs):
        return "<h1>" + fun(*args, **kwargs) + "</h2>"
    return add_func


def add_fun(fun):
    def add_func(*args, **kwargs):
        return "<td>" + fun(*args, **kwargs) + "</td>"
    return add_func



@set_fun
@add_fun
def test():
    return "hhhh"



print(test())
