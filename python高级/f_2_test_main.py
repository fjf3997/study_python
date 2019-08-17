import f_1_test as a
from imp import reload
if __name__ == '__main__':
    reload(a)
    print(a.age)
    print(a._age)