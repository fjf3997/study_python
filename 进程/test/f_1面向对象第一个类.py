class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


tom = Cat()
tom.name = "汤姆"
tom.drink()
tom.eat()
print(tom)
print(tom.name)
print("%x" % id(tom))
