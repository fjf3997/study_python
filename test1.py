# ==========while循环========
# i = int(input("请输入一个数字:"))
# n = 1
# s = 0
# =====当while 循环正常执行完，中间没有被break 中止的话，就会执行else后面的语句
# while n < 100:
#     s = s+n
#     n = n+1
#     # if n == 10:
#     #     break
# else:
#     print("循环结束")
# print(s)

# ==============占位符==============
# name = input('请输入姓名:')
# age = int(input('请输入年龄:'))
# sex = input("请输入性别:")
# msg = '''
# -----------inof of %s----------
# 姓名: %s
# 年龄: %d
# 性别: %s
# ''' % (name, name, age, sex)
# print(msg)
# ===========运算符===============
print(2 % 3)
print(2 ** 3)
print(3 // 2)
print(0 and 1)
print(0 and 0)
print(not 0)
print(3 > 4 or 4 < 3 and 1 == 1)
print(1 < 2 and 3 < 4 or 1 > 2)
print(4 or 8)
print(0 and 3)
print(3 and 4)
print(0 or 4 and 3 or 7 or 9 and 6)
print('喜欢' in '我喜欢你')
print('喜欢' not in '我喜欢你')
# ==========基础数据类型=========
num = -127
print(num.bit_length())
print(bool(100))
strNum = '123'
print(int(strNum))
a = "ABCDEFGHIJKLMN"
print(a[0:3])
print(a[:])
print(a[:-1])  #  -1 是列表中最后一个元素的索引，但是要满足顾头不顾腚的原则，所以取不到K元素
print(a[:5:2])  # 加步长
print(a[-1:-5:-2])  # 反向加步长
ret = a.count("D", 0, a.__len__())
print(ret)
print(a.startswith("ABC"))
print(a.endswith("KLMN"))
# split 以什么分割，最终形成一个列表此列表不含有这个分割的元素
split1 = "kfadjfajflkajdfjljgjdoajfkd".split('k')
print(split1)
split2 = "kfadjfajflkajdfjljgjdoajfkd".rsplit("k", 1)
print(split2)
#format的三种玩法 格式化输出
res = '{} {} {}'.format('egon', 18, 'male')
print(res)
res = '{1} {0} {1}'.format('egon', 18, 'male')
print(res)
res = '{name} {age} {sex}'.format(sex='male' , name='egon', age=18)
print(res)
#strip
name='*barry**'
print(name.strip('*'))
print(name.lstrip('*'))
print(name.rstrip('*'))
# replace
name = 'alex say :i have one tesla,my name is alex'
print(name.replace('alex', 'SB', 1))
name = 'taibai123'
print(name.isalnum())  # 字符串由字母或数字组成
print(name.isalpha())  # 字符串只由字母组成
print(name.isdecimal())  # 字符串只由十进制组成
# 寻找字符串中的元素是否存在
print(a)
ret2 = a.find("BCD", 2, 6)  # 返回的找到的元素的索引，如果找不到返回-1
print(ret2)
print(a.index("BCD", 1, 6))  # 返回的找到的元素的索引，找不到报错。
print(a.swapcase())  # 大小写翻转
msg = 'taibai say hi'
print(msg.title())  # 每个单词的首字母大写
# 内同居中，总长度，空白处填充
ret2 = msg.center(20, "*")
print(ret2)





