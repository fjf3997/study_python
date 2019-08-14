import socket


def main():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect(("192.168.198.1", 8080))
    send_data = input("请输入数据:")
    tcp_client.send(send_data.encode("gbk"))
    tcp_client.close()
    recv_data = tcp_client.recv(1024)
    print("接受到的数据:%s" % recv_data.decode("gbk"))


if __name__ == "__main__":
    main()

