import socket
import re


def server_response(new_socket):
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
    response = "HTTP/1.1 200 OK\r\n\r\n"
    try:
        f = open("html"+file_url, "rb")
        body = f.read()
        f.close()
    except Exception as result:
        response = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send("<h1>not found file</h1>".encode("utf-8"))
        print(result)
    else:
        new_socket.send(response.encode("utf-8"))
        new_socket.send(body)
    new_socket.close()


def main():
    web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    web_server.bind(("", 7890))
    web_server.listen(128)
    while True:
        temp_socket, client_address = web_server.accept()
        print("接受的的客户地址:", client_address)
        server_response(temp_socket)
    web_server.close()


if __name__ == "__main__":
    main()
