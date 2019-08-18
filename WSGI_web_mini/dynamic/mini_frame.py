import time
import re
from pymysql import connect

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.html")
def index():
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
            <input type="button" value="提交">
        </td>
    </tr>"""
    html = ""
    for one in my_stock_info:
        html += html_template % (one[0], one[1], one[2], one[3], one[4], one[5], one[6], one[7])
    content = re.sub(r"\{%content%\}", html, content)
    cs.close()
    conn.close()
    return content


@route("/register.html")
def register():
    return "------register---------%s" % time.ctime()


@route("/center.html")
def center():
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
                <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
            </td>
        </tr>"""
    html = ""
    for one in my_stock_info:
        html += html_template % (one[0], one[1], one[2], one[3], one[4], one[5], one[6])
    content = re.sub(r"\{%content%\}", html, content)
    cs.close()
    conn.close()
    return content

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
    try:
        return URL_FUNC_DICT[url]()
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
