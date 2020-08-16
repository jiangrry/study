# -*- coding: UTF-8 -*- 
# author(作者):jiangrry
"""
编写一个服务端和客户端，从客户端将一个文件上传给服务端，
注意文件类型可以为文本也可以是二进制文件。
接受文件 --> 客户端
"""

# 1.创建套接字对象
# 使用默认参数，——> tcp套接字
# 2.连接服务器
# 3.消息的收发
# 4.关闭套接字

from socket import *

sockdf = socket.socket()
sockdf.connect(("127.0.0.1", 8888))

file = open("tcp01.txt", "rb")
while True:
    data = file.read(2048)
    if not data:
        break
    sockdf.send(data)

sockdf.close()
file.close()
