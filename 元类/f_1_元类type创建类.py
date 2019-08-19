class Tes():
    num1 = 1
    pass


@classmethod
def test_class(cls):
    print("这是类方法.........")


@staticmethod
def test_static():
    print("这是静态方法")


def test_method(self):
    print("这是普通方法")


if __name__ == '__main__':

    Test = type("Test", (Tes,), {"num2": 2, "test_method": test_method, "test_class": test_class, "test_static": test_static})
    t = Test()
    print(Test.num1)
    print(Test.num2)
    print(t.num1)
    print(t.num2)
    Test.test_class()
    t.test_class()
    Test.test_static()
    t.test_static()
    t.test_method()
    # Test.test_method()
