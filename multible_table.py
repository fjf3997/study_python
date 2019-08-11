def mul_table():
    col = 1
    while col <= 9:
        row = 1
        while row <= col:
            print(("%d * %d = %d" % (row, col, row * col)), end='\t')
            row += 1
        print("")
        col += 1
