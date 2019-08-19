import time
import re
from pymysql import connect
import urllib.parse
import logging

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route(r"/index.html")
def index(ret):
    with open("./templates/index.html", encoding="utf-8") as f:
        content = f.read()
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    cs.execute("select * from info")
    result = cs.fetchall()
    # print(result)
    my_stock_info = result
    html_template = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
             <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
        </td>
    </tr>"""
    html = ""
    for one in my_stock_info:
        html += html_template % (one[0], one[1], one[2], one[3], one[4], one[5], one[6], one[7], one[1])
    content = re.sub(r"\{%content%\}", html, content)
    cs.close()
    conn.close()
    return content


@route(r"/register.html")
def register():
    return "------register---------%s" % time.ctime()


@route(r"/center.html")
def center(ret):
    with open("./templates/center.html", encoding="utf-8") as f:
        content = f.read()
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    cs.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from focus as f inner join info as i on i.id = f.info_id;")
    result = cs.fetchall()
    # print(result)
    my_stock_info = result
    html_template = """ <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>"""
    html = ""
    for one in my_stock_info:
        html += html_template % (one[0], one[1], one[2], one[3], one[4], one[5], one[6], one[0], one[0])
    content = re.sub(r"\{%content%\}", html, content)
    cs.close()
    conn.close()
    return content


@route(r"/add/(\d*)\.html")
def add_focus(ret):
    if ret:
        stock_code = ret.group(1)
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "select * from info where code =%s"
    cs.execute(sql, stock_code)
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票"
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "select * from info as i inner join focus as f on i.id = f.info_id where i.code = %s"
    cs.execute(sql, stock_code)
    if cs.fetchone():
        cs.close()
        conn.close()
        return "你已经关注过这支股票,请勿重复关注"
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "insert into focus(info_id) select i.id from info as i where i.code = %s; "
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "关注成功"


@route(r"/del/(\d*)\.html")
def del_focus(ret):
    if ret:
        stock_code = ret.group(1)
    else:
        return "服务器出现问题"
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "select * from info where code =%s"
    cs.execute(sql, stock_code)
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票"
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "select * from info as i inner join focus as f on i.id = f.info_id where i.code = %s"
    cs.execute(sql, stock_code)
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "你没有关注过这支股票"
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "delete from  focus where info_id = (select id from info where code =%s); "
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "取消关注成功"


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    if ret:
        stock_code = ret.group(1)
    else:
        return "服务器出现问题"
    with open("./templates/update.html", encoding="utf-8") as f:
        data = f.read()
    content = data
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "select f.note_info from focus as f inner join info as i on f.info_id = i.id where i.code = %s"
    cs.execute(sql, stock_code)
    result = cs.fetchone()
    cs.close()
    conn.close()
    content_result = result[0]
    content = re.sub(r"\{%note_info%\}", content_result, content)
    content = re.sub(r"\{%code%\}", stock_code, content)
    return content


@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    if ret:
        stock_code = ret.group(1)
        comment = ret.group(2)
        comment = urllib.parse.unquote(comment)
    else:
        return "出错了"
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = "update focus set note_info = %s where info_id = (select info.id from info where info.code = %s);"
    cs.execute(sql, (comment, stock_code))
    conn.commit()
    cs.close()
    conn.close()
    return "修改成功"
# URL_DICT = {
#     "/index.py": index,
#     "/register.py": register,
#     "/center.py": center
# }


def application(env, set_response_header):
    status = "200 OK"
    headers = [('Content-Type', 'text/html;charset=utf-8')]
    set_response_header(status, headers)
    url = env['PATH_INFO']
    logging.basicConfig(level=logging.INFO,
                        filename='./log.txt',
                        filemode='w',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    logging.info("用户访问的是%s" % url)
    try:
        for re_url, func in URL_FUNC_DICT.items():
            ret = re.match(re_url, url)
            if ret:
                print(re_url)
                return func(ret)
        else:
            logging.warning("请求的rul没有对应的函数%s" % url)
            return "请求的rul没有对应的函数%s" % url
    except Exception as rest:

        return "产生了异常%s" % rest
    # if url == "/index.py":
    #     return index()
    # elif url == "/register.py":
    #     return register()
    # elif url == "/center.py":
    #     return center()
    # else:
    #     return "not found your request"

# def application(url):
#     if url == "/login.py":
#         return login()
#     elif url == "/register.py":
#         return register()
#     elif url == "/logout.py":
#         return logout()
#     else:
#         return "not found your request"
