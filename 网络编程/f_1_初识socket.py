import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 1234))
    while True:
        send_data = input("请输入发送内容:")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("gbk"), ("192.168.198.1", 8080))
    udp_socket.close()


if __name__ == "__main__":
    main()
