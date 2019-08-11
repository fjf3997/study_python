def test(num):
    print("函数内部遍历的地址是%d" % id(num))
    result = "hello"
    print("函数内%s的内存地址是%d" % (result, id(result)))
    return  result


a = 1
print("a的内存地址是%d" % id(a))
print("字符a的内存地址是%d" % id("a"))
result = test(a)
print("函数外%s的内存地址是%d" % (result, id(result)))
