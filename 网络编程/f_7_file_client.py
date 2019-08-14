import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8888))
    filename = input("请输入文件名字:")
    client_socket.send(filename.encode("gbk"))
    data_recv = client_socket.recv(1024)
    if data_recv:
        with open("[文件]"+filename, "wb") as f:
                f.write(data_recv)
    client_socket.close()


if __name__ == "__main__":
    main()
