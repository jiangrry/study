# -*- coding: UTF-8 -*- 
# author(作者):jiangrry
import socket

# 1. 创建 tcp 套接字对象
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定地址
sockfd.bind(("127.0.0.1", 8888))

# 3. 设置监听
sockfd.listen(5)

# 4. 等待 处理客户端链接
print("Waiting For Connent...")
connfd, addr = sockfd.accept()
print("Connent From...", addr)

# 5. 收发消息
data = connfd.recv(1024)
print("收到:", data.decode())
number = connfd.send(b'Thanks')
print("发送%d个字节数" % number)

# 6. 关闭套接字
connfd.close()
sockfd.close()
