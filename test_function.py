import multible_table


def sum_2_num(num1, num2):
    result = num1 + num2
    # print("%d + %d = %d" % (num1, num2, result))
    multible_table.mul_table()
    return result


def print_line(char, count, line_num):
    """打印任意行注释

    :param char: 符号
    :param count: 每行打印次数
    :param line_num: 打印的函数
    """
    c = 0
    # if type(char) == int:
    #     char = chr(char)
    #     print('转换int类型的char')
    # print(type(char))
    while c < line_num:
        print(char * count)
        c += 1


# result = sum_2_num(10, 20)
# print('函数返回的结果:%d' % result)
print_line('*', 50, 5)

