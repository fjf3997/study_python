class Product:
    def __init__(self):
        self.price_ = 100

    def get_price(self):
        return self.price_

    def set_price(self, value):
        self.price_ = value

    def del_price(self):
        del self.price_

    price = property(get_price, set_price, del_price, "描述")


if __name__ == '__main__':
    p = Product()
    print(p.price)
    p.price = 200
    print(p.price)
    desc = Product.price.__doc__
    print(desc)
    del p.price
    # print(p.price)

