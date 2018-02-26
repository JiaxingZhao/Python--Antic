from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread


class RecvMessage(Thread):
    def __init__(self, udp_socket):
        super().__init__()
        self.udp_socket = udp_socket

    def run(self):
        self.recv_data()

    def recv_data(self):
        while True:
            recv_msg = self.udp_socket.recvfrom(1024)
            print("接收到的信息：", recv_msg[0])


class SendMessage(Thread):
    def __init__(self, udp_socket, target_host, target_port):
        super().__init__()
        self.udp_socket = udp_socket
        self.target_host = target_host
        self.target_port = target_port

    def run(self):
        self.send_data()

    def send_data(self):
        while True:
            send_msg = input("发送消息：")
            self.udp_socket.sendto(send_msg.encode(
                "gb2312"), (self.target_host, self.target_port))


class ChatSystem(object):
    def start(self):
        udp_socket = socket(AF_INET, SOCK_DGRAM)
        target_host = input("目标主机地址：")
        target_port = int(input("目标主机端口："))
        udp_socket.bind(("", 8082))

        RecvMessage(udp_socket).start()
        SendMessage(udp_socket, target_host, target_port).start()


if __name__ == "__main__":
    ChatSystem().start()
