class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("蹦蹦跳跳的%s" % self.name)


class Tiangou(Dog):
    def game(self):
        print("能飞天狗%s" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s和%s一起玩耍" % (self.name, dog.name))
        dog.game()


# wangcai = Dog("旺财")
wangcai = Tiangou("旺财")
xiaoming = Person("小明")
xiaoming.play_with_dog(wangcai)
