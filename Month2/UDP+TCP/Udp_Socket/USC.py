# -*- coding: UTF-8 -*- 
# author(作者):jiangrry
from socket import *

# 1. 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)  # 不能使用默认

ADDR = ("127.0.0.1", 8888)

# 2. 循环收发消息
while True:
    msg = input("Msg>>> ")
    if not msg:
        break
    sockfd.sendto(msg.encode(), ADDR)
    data, addr = sockfd.recvfrom(1024)
    print("Response: ", data.decode())

# 3. 关闭套接字
sockfd.close()
