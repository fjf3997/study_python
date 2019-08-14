import os
import multiprocessing
import time
import random


def copy_file(q, name, old_folder, new_folder):
    # print("正在拷贝文件%s" % name)
    source = open(old_folder + "/" + name, "rb")
    content = source.read()
    # print(content)
    source.close()
    target = open(new_folder+"/"+name, "wb")
    target.write(content)
    target.close()
    time.sleep(random.random())
    q.put(name)


def main():
    old_folder = input("请输入要拷贝的文件夹:")
    new_folder = old_folder+"[复件]"
    try:
        os.mkdir(new_folder)
    except:
        pass
    file_names = os.listdir(old_folder)
    # for name in file_names:
    #     print(name)
    po = multiprocessing.Pool(5)
    q = multiprocessing.Manager().Queue()
    for name in file_names:
        po.apply_async(copy_file, (q, name, old_folder, new_folder))

    po.close()
    total_file_num = len(file_names)
    file_ok_num = 0

    while True:
        name = q.get()
        if name:
            file_ok_num += 1
        print("\r下载进度为%.2f %%" % (file_ok_num*100/total_file_num), end="")
        if file_ok_num >= total_file_num:
            break
        print()
    # po.join()


if __name__ == "__main__":
    main()
