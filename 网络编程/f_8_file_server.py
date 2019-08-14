import socket


def file_2_client(new_socket, address_client):
    filename = new_socket.recv(1024).decode("gbk")
    print("客户端%s要下载的文件是:%s" % (str(address_client), filename))
    file_content = None
    try:
        f = open(filename, "rb")
        file_content = f.read()
        f.close()
    except Exception as result:
        print("没有%s文件" % filename)
    if file_content:
        new_socket.send(file_content)


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(("", 8888))
    tcp_server.listen(128)

    while True:
        new_socket, address_client = tcp_server.accept()
        print(address_client)
        file_2_client(new_socket, address_client)
        new_socket.close()
    tcp_server.close()


if __name__ == "__main__":
    main()
