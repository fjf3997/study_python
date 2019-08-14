import time
import threading


def sing():
    for i in range(5):
        print("唱歌,好嗨哦...........")
        time.sleep(1)


def dance():
    for i in range(5):
        print("跳舞,大象舞..........")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    # for i in range(5):
    #     print(threading.enumerate())
    #     time.sleep(1)
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()

