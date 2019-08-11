g_num_list = [1, 2, 3]


def fun(num_list):
    num_list.append(4)
    print(num_list)
    print("函数调用结束")


print(g_num_list)
fun(g_num_list)
print(g_num_list)