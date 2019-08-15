class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count
        print("增加子弹%d" % count)

    def shot(self):
        if self.bullet_count <= 0:
            print("%s没有子弹" % self.model)
            return
        self.bullet_count -= 1
        print("突突突,..发射子弹,剩余%d子弹" % self.bullet_count)

    def __str__(self):
        return "%s,子弹数量:%d" % (self.model, self.bullet_count)


class Solider:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def shot(self):
        if self.gun is None:
            print("%s还没有枪,你打毛线,,,," % self.name)
            return
        self.gun.add_bullet(12)
        self.gun.shot()


ak = Gun("AK47")
ak.add_bullet(50)
ak.shot()
ak.shot()
ak.shot()
ak.shot()
print(ak)

xu = Solider("张三")
xu.gun = ak
xu.shot()
