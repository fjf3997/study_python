def digui(num):
    if num == 1:
        return 1
    temp = digui(num-1)
    return num + temp


result = digui(2)
print(result)
