# -*- coding: UTF-8 -*- 
# author(作者):jiangrry

from socket import *

sockdf = socket(AF_INET, SOCK_DGRAM)

ADDR = ("127.0.0.1", 8888)
while True:
    data = input("word>>>")
    if not data:
        break
    sockdf.sendto(data.encode(), ADDR)
    msg, addr = sockdf.recvfrom(1024)
    print(msg.decode())

sockdf.close()
