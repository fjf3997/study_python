import socket
import threading


def socket_rec(udp_socket):
    while True:
        data = udp_socket.recvfrom(1024)
        content = data[0].decode("gbk")
        print(content)


def socket_send(udp_socket, socket_ip, socket_port):
    while True:
        data = input("请输入要输入的内容:")
        udp_socket.sendto(data.encode("gbk"), (socket_ip, socket_port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 8888))
    socket_ip = "192.168.198.1"
    socket_port = 8080
    t1 = threading.Thread(target=socket_rec, args=(udp_socket,))
    t2 = threading.Thread(target=socket_send, args=(udp_socket, socket_ip, socket_port))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
