from pymysql import connect


class JD:
    def __init__(self):
        self.__conn = connect(host="localhost", port=3306, database="jing_dong", user="root", password="root", charset="utf8")
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()

    def cursor_execute(self, sql):
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        for one in result:
            print(one)

    def find_all_product(self):
        sql = "select * from goods"
        self.cursor_execute(sql)

    def find_all_cates(self):
        sql = "select name from goods_cates"
        self.cursor_execute(sql)

    def find_all_brands(self):
        sql = "select name from goods_brands"
        self.cursor_execute(sql)

    def add_brand(self):
        brand_name = input("请输入品牌名称:")
        sql = "insert into goods_brands values (null,'%s')" % brand_name
        self.__cursor.execute(sql)
        self.__conn.commit()

    def find_one_by_name(self):
        name = input("请输入商品的名称:")
        sql = "select * from goods where name =%s"
        self.__cursor.execute(sql,[name])
        print(self.__cursor.fetchall())

    @staticmethod
    def print():
        print("------数据库练习 --------")
        print("1.查询所有商品所有信息")
        print("2.查询所有商品类别")
        print("3,查询所有品牌")
        print("4.添加商品品牌")
        print("5.查询一个商品信息")
        return input("请输入你的选择:")

    def run(self):
        while True:

            num = self.print()

            if num == "1":
                self.find_all_product()
            elif num == "2":
                self.find_all_cates()
            elif num == "3":
                self.find_all_brands()
            elif num == "4":
                self.add_brand()
            elif num == "5":
                self.find_one_by_name()
            else:
                print("输入有误")


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()