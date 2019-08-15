def create_num(num):
    current_num = 0
    a = 0
    b = 1
    while current_num < num:
        yield a
        a, b = b, a+b
        current_num += 1
    return "over"

def main():
    obj = create_num(10)
    # for i in obj:
    #     print(i)
    while True:
        try:
            tem = next(obj)
            print(tem)
        except Exception as result:
            print(result.value)
            break


if __name__ == "__main__":
    main()
