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


name = '樊家富'
