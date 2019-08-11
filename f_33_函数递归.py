def digui(num):
    print(num)
    if num == 0:
        return
    digui(num - 1)
    print("函数调用%s" % num)

digui(3)