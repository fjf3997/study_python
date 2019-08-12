try:
    num = int(input("请输入一个整数: "))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除零错误")
except ValueError:
    print("输入值错误")
except Exception as result:
    print("未知错误:%s" % result)
else:
    print("没有异常")
finally:
    print("异常捕获结束")

print("_"*50)