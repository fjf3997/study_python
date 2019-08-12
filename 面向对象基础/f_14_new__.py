class MusicPlay:
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print("new方法内部:分配空间,返回实例引用")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not MusicPlay.init_flag:
            print("对象初始化完成")
            MusicPlay.init_flag = True
        else:
            return


qqPlay = MusicPlay()
play2 = MusicPlay()
print(qqPlay)
print(play2)
