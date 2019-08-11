def fun():
    temp = 24
    wetness = 34
    return temp, wetness


result = fun()
print(type(result))
print(result)
# 接受多个返回值
g_temp, g_wetness = fun()
print(g_temp)
print(g_wetness)
