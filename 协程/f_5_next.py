def test(num):
    curr = 0
    a = 0
    b = 1
    while curr < num:
        temp = yield a
        print("接受send的值:", temp)
        a, b = b, a+b
        curr += 1


if __name__ == "__main__":
    obj = test(3)
    ret = next(obj)
    print(ret)
    ret = obj.send("hhhh")
    print(ret)
    ret = next(obj)
    print(ret)
