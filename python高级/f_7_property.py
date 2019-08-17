class Product:
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        return self.original_price*self.discount

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


if __name__ == '__main__':
    p = Product()
    print(p.price)
    p.price = 200
    print(p.price)
    del p.price
    # print(p.price)
