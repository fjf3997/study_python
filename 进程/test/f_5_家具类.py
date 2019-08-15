class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] :占地面积为%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.freeArea = area
        self.item = []

    def __str__(self):
        return ("户型[%s],占地面积%.2f,剩余面积%.2f,所有家具%s"
                % (self.house_type, self.area, self.freeArea, self.item))

    def add_item(self, item):
        if self.freeArea < item.area:
            print("面积不足够添加家具:%s" % item.name)
            return
        print("添加家具:%s" % item)
        self.freeArea -= item.area
        self.item.append(item.name)


bed = HouseItem("席梦思", 4)
print(bed)
chest = HouseItem("衣柜", 2)
print(chest)
table = HouseItem("桌子", 1.5)
print(table)
house = House("三室一厅", 5)
print(house)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
