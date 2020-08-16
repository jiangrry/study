# -*- coding: UTF-8 -*- 
# author(作者):jiangrry

"""
编写一个服务端和客户端，从客户端将一个文件上传给服务端，
注意文件类型可以为文本也可以是二进制文件。
接受文件 --> 服务端
"""

# 1. 创建 tcp 套接字对象
# 2. 绑定地址
# 3. 设置监听
# 4. 等待 处理客户端链接
# 5. 收发消息
# 6. 关闭套接字


from socket import *

sockdf = socket()
sockdf.bind(("127.0.0.1", 8888))
sockdf.listen(6)

connfd, addr = sockdf.accept()
print("Connect From", addr)

file = open("tcp01.txt", "wb")
while True:
    data = connfd.recv()
    if not data:
        break
    file.write(data)

file.close()
connfd.close()
sockdf.close()
