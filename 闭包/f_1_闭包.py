def y(k, b):
    def create_y(x):
        print(k*x+b)
    return create_y


y1 = y(2,4)
print(type(y1))
y1(1)
y1(2)
y1(3)
x = 300
def test1():
    x = 200

    def test2():
        global x
        print("-----------x%d----------" % x)
        x = 100
        print("-----------x%d----------" % x)
    return test2

t = test1()
t()
