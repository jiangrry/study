# -*- coding: UTF-8 -*- 
# author(作者):jiangrry

from socket import *

# 1.创建套接字对象
# 使用默认参数，——> tcp套接字

sockfd = socket()

# 2.连接服务器
server_addr = ("127.0.0.1", 8888)  # 服务器地址和端口号
sockfd.connect(server_addr)

# 3.消息的收发
msg = input("MSG: >>>>")
sockfd.send(msg.encode())
data = sockfd.recv(1024)
print("Server data:", data.decode())

# 4.关闭套接字
sockfd.close()
