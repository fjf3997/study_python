class Cat:
    def __init__(self, new_name):
        print("init方法调用")
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("del方法调用")


tom = Cat("汤姆")
print(tom.name)
tom.eat()
del tom
print("-"*50)
