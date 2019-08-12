class Animal:
    def __init__(self):
        self.name = "狗"
        self.__age = 10

    def eat(self):
        print("吃%d" % self.__age)

    def drink(self):
        print("喝")

    def play(self):
        print("完")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("旺旺叫.........%s" % self.name)
        print(self._Animal__age)



class Xiaotianquan(Dog):
    def fly(self):
        print("我会飞")

    # 重写
    def bark(self):
        # super().bark()  # 扩展
        Dog.bark(self)
        print("我还会说人话")
        # print(self._Dog__age)


wangcai = Xiaotianquan()
wangcai.eat()
wangcai.drink()
wangcai.play()
wangcai.sleep()
wangcai.bark()
wangcai.fly()
print(wangcai.name)
