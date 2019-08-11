g_num = 100
g_num_list = [1, 2, 3]


def fun(num, num_list):
    num += num
    num_list += num_list
    print("函数内部")
    print(num)
    print(num_list)
    print("函数调用结束")


fun(g_num, g_num_list)
print(g_num)
print(g_num_list)

