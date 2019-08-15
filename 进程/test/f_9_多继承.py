class A:
    def demo1(self):
        print("A类的demo测试")

    def test1(self):
        print("A类的test测试")


class B:
    def test1(self):
        print("B类的test测试")

    def demo1(self):
        print("B类的demo测试")


class C(B, A):
    pass


c = C()
c.demo1()
c.test1()
print(dir(c))
print(C.__mro__)