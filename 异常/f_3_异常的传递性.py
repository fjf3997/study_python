def demo1():
    return int(input("请输入一个整数: "))


def demo2():
    return demo1()


try:
    demo2()
except Exception as result:
    print("错误:%s" % result)
