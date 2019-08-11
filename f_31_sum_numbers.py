def sum(*args):

    print(args)
    sum = 0
    for arg in args:
        sum += arg
    return sum


result = sum(1, 2, 3, 4, 5,)
print(result)

