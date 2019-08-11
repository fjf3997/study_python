def demo(*args, **kwargs):
    print(args)
    print(kwargs)


g_list = [1, 2, 3, 4]
g_tuple = {"name": "樊家富", "age": 18}
demo(g_list, g_tuple)
demo(*g_list, **g_tuple)