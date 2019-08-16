import socket
import time
import re
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setblocking(False)
socket_server.bind(("", 8888))
socket_server.listen(128)
socket_list = list()


def server_response(new_socket, recv_data):
    recv_content = recv_data.decode("utf-8")
    request_lines = recv_content.splitlines()
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

    try:
        f = open("html"+file_url, "rb")
        response_body = f.read()
        f.close()
    except Exception as result:
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = "<h1>not found file</h1>".encode("utf-8")
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)
    else:
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)


def main():
    while True:
        # time.sleep(0.5)
        try:
            temp_socket, socket_address = socket_server.accept()
        except:
            # print("用户还没到来")
            pass
        else:
            print("用户到来,地址:", socket_address)
            temp_socket.setblocking(False)
            socket_list.append(temp_socket)

        for socket_one in socket_list:
            try:
                recv_data = socket_one.recv(1024)
            except:
                # print("客户端还未发送数据")
                pass
            else:
                if recv_data:
                    server_response(socket_one, recv_data)
                else:
                    socket_one.close()
                    socket_list.remove(socket_one)
                    print("关闭客户端套接字")
    socket_server.close()


if __name__ == "__main__":
    main()
