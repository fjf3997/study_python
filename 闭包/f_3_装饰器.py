import time


def add_function(fun1,fun2):
    def add_fun(num):
        start_time = time.time()
        fun1(num)
        fun2()
        end_time = time.time()
        print("执行时间为:%f" % (end_time - start_time))
    return add_fun


# @add_function
def test1(num):
    print("---------test1------%d" % num)
    for i in range(100000000):
        pass


# @add_function
def test2():
    print("----------test2--------------")


# test1()
test1 = add_function(test1, test2)
test1(100)
