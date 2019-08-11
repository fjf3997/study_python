a = 100
b = 99
# 方法一
a = a + b
b = a - b
a = a - b
print(a)
print(b)
# python专用方法
a, b = b, a
print(a)
print(b)

