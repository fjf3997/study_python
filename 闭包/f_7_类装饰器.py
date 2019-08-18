class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("装饰类的添加")
        return self.func(*args, **kwargs)


@Test
def test(num):
    return "hhhhh---------%d" % num


if __name__ == '__main__':
    print(test(100))
