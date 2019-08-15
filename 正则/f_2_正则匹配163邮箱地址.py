import re


def main():
    while True:
        name = input("请输入邮箱地址:")
        ret = re.match(r"^[a-zA-Z0-9_]{4,20}@(163|qq)\.com$", name)
        if ret is not None:
            print("%s符合邮箱,正则匹配的为%s" % (name, ret.group()))
        else:
            print("%s不符合邮箱要求" % name)


if __name__ == "__main__":
    main()
