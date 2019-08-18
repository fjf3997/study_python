def set_level(level_num):
    def set_fun(func):
        def call_fun():
            if level_num == 1:
                print("---------权限一级---")
            elif level_num == 2:
                print("--------权限二级-----")
            func()
        return call_fun
    return set_fun


@set_level(1)
def test1():
    print("-----test1-------")


@set_level(2)
def test2():
    print("-------test2--------")


if __name__ == '__main__':
    test1()
    test2()