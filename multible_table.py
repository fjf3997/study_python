def mul_table():
    """打印九九乘法表 """
    col = 1
    while col <= 9:
        row = 1
        while row <= col:
            print(("%d * %d = %d" % (row, col, row * col)), end='\t')
            row += 1
        print("")
        col += 1


# print('打印九九乘法表开始')
# mul_table()
# print('打印九九乘法表结束')
