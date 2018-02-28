from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread


def recv_data(new_socket, new_address):
    while True:
        recv_msg = new_socket.recv(1024).decode("gb2312")
        if recv_msg:
            print("收到消息：{}".format(recv_msg))
            new_socket.send("THANKS!".encode("gb2312"))
        if not recv_msg:
            print("连接丢失，已断开")
            break


def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_socket.bind(("", 8080))
    tcp_socket.listen(5)
    while True:
        new_socket, new_address = tcp_socket.accept()
        Thread(target=recv_data, args=(new_socket, new_address)).start()
    tcp_socket.close()


if __name__ == '__main__':
    main()
