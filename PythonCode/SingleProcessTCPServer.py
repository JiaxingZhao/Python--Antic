from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_socket.bind(("", 8080))
    tcp_socket.listen(5)

    while True:
        new_socket, new_address = tcp_socket.accept()
        while True:
            recv_msg = new_socket.recv(1024).decode("gb2312")
            if recv_msg:
                print("收到消息：{}".format(recv_msg))
                new_socket.send("THANKS!".encode("gb2312"))
            if not recv_msg:
                print("连接丢失，已断开")
                new_socket.close()
                break
    tcp_socket.close()
    print("关闭{}客户端".format(new_address))


if __name__ == '__main__':
    main()
