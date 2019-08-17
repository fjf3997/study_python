import pymysql


def main():
    conn = pymysql.connect(host="localhost", port=3306, database="jing_dong", user="root", password="root", charset="utf8")
    cs1 = conn.cursor()
    result = cs1.execute("select * from goods")
    for one in cs1.fetchall():
        print(one)
    # print(result)
    cs1.close()
    conn.close()



if __name__ == '__main__':
    main()