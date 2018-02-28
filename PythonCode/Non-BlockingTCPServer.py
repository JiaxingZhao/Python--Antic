from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_socket.bind(("", 8080))
tcp_socket.listen(5)
tcp_socket.setblocking(False)
client_list = []

while True:
    try:
        new_socket, new_address = tcp_socket.accept()
    except Exception as result:
        pass
    else:
        print("有新的连接：{}".format(new_address))
        new_socket.setblocking(False)
        client_list.append((new_socket, new_address))

    for new_socket, new_address in client_list:
        try:
            recv_msg = new_socket.recv(1024).decode("gb2312")
        except Exception as result:
            pass
        else:
            if recv_msg:
                print("收到信息：{}".format(recv_msg))
                new_socket.send("已经收到信息：{}".format(recv_msg).encode("gb2312"))
            if not recv_msg:
                print("{}连接丢失，已断开".format(new_address))
                client_list.remove((new_socket, new_address))
tcp_socket.close()
