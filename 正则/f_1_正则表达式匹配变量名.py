import re


def main():
    names = ["_name", "__name", "3name", "__name__", "a!we", "adf$"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret is not None:
            print("%s符合变量名,正则匹配的为%s" % (name, ret.group()))
        else:
            print("%s不符合变量名要求" % name)


if __name__ == "__main__":
    main()
