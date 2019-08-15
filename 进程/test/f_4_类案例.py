class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sport(self):
        self.weight -= 1

    def eat(self):
        self.weight += 1

    def __str__(self):
        return "%s目前的体重是%d" % (self.name, self.weight)

    def __del__(self):
        print("对象销毁")


xiaoming = Person("小明", 80)
print(xiaoming)
xiaoming.sport()
print(xiaoming)
xiaoming.eat()
print(xiaoming)
