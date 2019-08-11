# 判断是否是空串
str = "           \t\n\r"
print(str.isspace())
# 判断是否是数字 **都不能判断小数
str_num1 = "1"
print(str_num1)
print(str_num1.isdecimal())
print(str_num1.isdigit())
print(str_num1.isnumeric())
str_num2 = "\u00b2"
print(str_num2)
print(str_num2.isdecimal())
print(str_num2.isdigit())
print(str_num2.isnumeric())
str_num3 = "一千零一"
print(str_num3)
print(str_num3.isdecimal())
print(str_num3.isdigit())
print(str_num3.isnumeric())
