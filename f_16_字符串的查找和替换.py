str = "hello,world"
# 字符串是否以什么开始
print(str.startswith("hell"))
# 字符串是否以什么结束
print(str.endswith("rld"))
# 查找子字符串
print(str.find("llo"))
print(str.find("abc"))
# 字符串的替换
newstr = str.replace("world", "python")
print(newstr)
print(str)
