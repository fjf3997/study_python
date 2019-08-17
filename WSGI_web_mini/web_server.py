import socket
import re
import multiprocessing
import time


class WsgiServer:
    def __init__(self):
        self.web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.web_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.web_server.bind(("", 7890))
        self.web_server.listen(128)

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
        header = "HTTP/1.1 200 OK\r\n\r\n"
        if file_url.endswith(".py"):
            header = "HTTP/1.1 200 OK\r\n\r\n"
            body = "hhhhh%s" % time.ctime()
            response = header + body
            new_socket.send(response.encode("utf-8"))
            return

        try:
            f = open("html"+file_url, "rb")
            body = f.read()
            f.close()
        except Exception as result:
            header = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
            new_socket.send(header.encode("utf-8"))
            new_socket.send("<h1>not found file</h1>".encode("utf-8"))
            print(result)
        else:
            new_socket.send(header.encode("utf-8"))
            new_socket.send(body)
        finally:
            print("专用套接字关闭")
            new_socket.close()

    def run_server(self):

        while True:
            temp_socket, client_address = self.web_server.accept()
            print("接受的的客户地址:", client_address)
            p = multiprocessing.Process(target=self.server_response, args=(temp_socket,))
            p.start()
            temp_socket.close()
        self.web_server.close()


def main():
    web_server = WsgiServer()
    web_server.run_server()


if __name__ == "__main__":
    main()
