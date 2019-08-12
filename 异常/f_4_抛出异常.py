def login():
    num = input("请输入密码: ")
    if len(num) > 8:
        return num
    print("主动抛出异常")
    ex = Exception("密码长度不够")
    raise ex

try:
    print(login())
except Exception as result:
    print(result)
