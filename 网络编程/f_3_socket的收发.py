import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_ip = input("请输入ip地址:")
    send_port = int(input("请输入端口号:"))
    send_bind = (send_ip, send_port)
    udp_socket.bind(("192.168.198.1", 8888))
    send_data = input("请输入发送内容:")
    udp_socket.sendto(send_data.encode("gbk"), send_bind)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode("gbk"))
    udp_socket.close()


if __name__ == "__main__":
    main()

