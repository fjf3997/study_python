num = 100


def fun1():
    # 修改全局变量
    global num
    num = 99
    print("输出num结果%d" % num)


def fun2():
    print("输出num结果%d" % num)


fun1()
fun2()
