import socket


def main():
    udp_socket =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address_bind = ("", 8888)
    udp_socket.bind(address_bind)
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_content = recv_data[0]
        recv_address = recv_data[1]
        print("%s:%s" % (str(recv_address), recv_content.decode("gbk")))
    udp_socket.close()


if __name__ == "__main__":
    main()
