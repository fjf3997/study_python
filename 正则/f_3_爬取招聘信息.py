import urllib.request
import re


def main():
    req = urllib.request.urlopen("https://www.baidu.com")
    content = (req.read()).decode("utf-8")
    print(content)
    print("------------------------------")
    ret = re.findall(r"http:.*\.com/", content)
    print(ret)


if __name__ == "__main__":
    main()
