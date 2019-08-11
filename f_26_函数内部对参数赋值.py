g_num = 100
g_num_list = [1,2,3]


def fun(num, num_list):

    print(id(num))
    print(id(num_list))
    num = 99
    num_list = [4, 5, 6]
    print(id(num))
    print(id(num_list))
    print(num)
    print(num_list)


print(id(g_num))
print(id(g_num_list))
fun(g_num, g_num_list)
print(g_num)
print(g_num_list)
print(id(g_num))
print(id(g_num_list))
