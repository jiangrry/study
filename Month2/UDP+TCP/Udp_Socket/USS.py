# -*- coding: UTF-8 -*- 
# author(作者):jiangrry
from socket import *

# 1. 创建套接字
#  第一个参数： ipv4 ； 第二个参数： UDP编程 --> 不能选择默认
sockfd = socket(AF_INET, SOCK_DGRAM)

# 2. 绑定地址
server_addr = ("127.0.0.1", 8888)
sockfd.bind(server_addr)

# 3. 循环收发消息
while True:
    try:
        # data, addr = sockfd.recvfrom(1024)
        data, addr = sockfd.recvfrom(5)  #
    except KeyboardInterrupt:
        break
    print("From clinet %s ,Msg: %s" % (addr, data.decode()))
    sockfd.sendto(b'Thanks', addr)

# 4. 关闭套接字
sockfd.close()
