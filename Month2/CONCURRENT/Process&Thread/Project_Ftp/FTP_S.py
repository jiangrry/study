# -*- coding: UTF-8 -*- 
# author(作者):jiangrry

from socket import *
from threading import *
import sys, os

# 全局变量
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
FTP = "E:\Month2\Process+Thread\Project_Ftp/"  # 文件位置


# 客户端处理类 查看服务器，上传，下载
class FTPServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def run(self) -> None:
        # 接收客户端发送的请求
        while True:
            data = self.connfd.recv(1024).decode()
            # print(data)
            if not data or data == 'Q':
                return
            elif data == 'L':
                self.do_list()


# 搭建网络模型
def main():
    # 创建tcp套接字

    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
    print(" Listen the port 8888 ")
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue
        t = FTPServer(c)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
