import socket
import re
import select


def server_response(new_socket, recv_data):
    recv_content = recv_data.decode("utf-8")
    request_lines = recv_content.splitlines()
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

    try:
        f = open("html"+file_url, "rb")
        response_body = f.read()
        f.close()
    except Exception as result:
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = "<h1>not found file</h1>".encode("utf-8")
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)
    else:
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)


def main():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setblocking(False)
    socket_server.bind(("", 8888))
    socket_server.listen(128)
    epl = select.epoll()
    epl.register(socket_server.fileno(), select.EPOLLIN)
    fd_event_dict = dict()

    while True:
        event_list = epl.poll()
        for fd, event in event_list:
            if fd == socket_server.fileno():
                new_socket,client_address = socket_server.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                new_socket = fd_event_dict[fd]
                recv_data = new_socket.recv(1024)
                if recv_data:
                    server_response(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    socket_server.close()


if __name__ == "__main__":
    main()
