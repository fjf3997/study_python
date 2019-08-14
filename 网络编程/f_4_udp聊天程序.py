import socket


def send_msg(udp_socket):
    send_ip = input("请输入ip地址:")
    send_port = int(input("请输入端口号:"))
    send_bind = (send_ip, send_port)
    send_data = input("请输入发送内容:")
    udp_socket.sendto(send_data.encode("gbk"), send_bind)


def recv_meg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("192.168.198.1", 8888))
    while True:
        print("******聊天系统******")
        print("1.发送数据")
        print("2.接受数据")
        print("0.退出")
        op = input("请输入与你的选择:")
        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_meg(udp_socket)
        elif op == "0":
            exit()
        else:
            print("输入有误")
    udp_socket.close()


if __name__ == "__main__":
    main()
