import socket
import re
import multiprocessing
import time
import sys
import dynamic.mini_frame


class WsgiServer:
    def __init__(self, application, port, static_path):
        self.web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.web_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.web_server.bind(("", port))
        self.web_server.listen(128)
        self.application = application
        self.static_path = static_path
    def server_response(self, new_socket):
        # header = ""
        # body = ""
        # response = ""
        # file_url = ""
        data = new_socket.recv(1024)
        revc_content = data.decode("utf-8")
        request_lines = revc_content.splitlines()
        # for line in request_lines:
        #     print(line)
        fist_line = request_lines[0]
        # print(fist_line)
        ret = re.match(r"[^/]*([^ ]*)", fist_line)
        if ret:
            file_url = ret.group(1)
            if file_url == "/":
                file_url = "/index.html"
            # print(file_url)

        # if file_url.endswith(".py"):
        #     header = "HTTP/1.1 200 OK\r\n\r\n"
        #     body = "hhhhh%s" % time.ctime()
        #     response = header + body
        #     new_socket.send(response.encode("utf-8"))
        #     return
        if not file_url.endswith(".py"):
            try:
                f = open(self.static_path+file_url, "rb")
                body = f.read()
                f.close()
            except Exception as result:
                header = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
                new_socket.send(header.encode("utf-8"))
                new_socket.send("<h1>not found file</h1>".encode("utf-8"))
                print(result)
            else:
                header = "HTTP/1.1 200 OK\r\n\r\n"
                new_socket.send(header.encode("utf-8"))
                new_socket.send(body)
        else:
            env = dict()
            env['PATH_INFO'] = file_url
            body = self.application(env, self.set_response_header)
            header = "HTTP/1.1 " + self.status + "\r\n"
            for one in self.headers:
                header += "%s:%s\r\n" % (one[0], one[1])
            header += "\r\n"
            response = header + body
            new_socket.send(response.encode("utf-8"))
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [('server', 'fjf_server')]
        self.headers += headers

    def run_server(self):

        while True:
            temp_socket, client_address = self.web_server.accept()
            print("接受的的客户地址:", client_address)
            p = multiprocessing.Process(target=self.server_response, args=(temp_socket,))
            p.start()
            temp_socket.close()
        self.web_server.close()


def main():
    arg = sys.argv
    if len(arg) == 3:
        try:
            port = int(arg[1])
            frame_app = arg[2]
        except Exception as res:
            print(res)
            print("端口号请输入数字:")
    print(port, frame_app)
    ret = re.match(r"([^:]+):(.*)", frame_app)
    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
    else:
        print("请按照以下方式运行程序:")
        print("python xxx.py port xxx:xxx")
        return
    with open("web_server.conf") as f:
        eva = eval(f.read())
    sys.path.append(eva["dynamic_path"])
    frame = __import__(frame_name)
    app = getattr(frame, app_name)
    web_server = WsgiServer(app, port, eva["static_path"])
    web_server.run_server()


if __name__ == "__main__":
    main()
