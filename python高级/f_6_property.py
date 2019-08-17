class G:
    def __init__(self):
        self.name_ = "fjf"

    @property
    def name(self):
        return self.name_


if __name__ == '__main__':
    g = G()
    print(g.name)
