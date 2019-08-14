import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 8888))
    tcp_server_socket.listen(128)
    while True:
        print("等待一个新的客户端")
        new_socket, client_addr = tcp_server_socket.accept()
        print("收到一个新的客户端:%s" % str(client_addr))
        # print(new_socket)
        while True:
            recv_data = new_socket.recv(1024)
            if not recv_data:
                break
            content = recv_data.decode("gbk")
            if content == "q":
                break

            print("收到的数据为:%s" % content)
            new_socket.send("你好,很高兴为你服务".encode("gbk"))
        new_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
