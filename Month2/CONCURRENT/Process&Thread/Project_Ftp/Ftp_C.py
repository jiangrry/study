# -*- coding: UTF-8 -*- 
# author(作者):jiangrry
"""
ftp 文件服务器服务端
env : python 3
多线程 tcp并发
"""

from socket import *
from threading import *
import sys, os

from socket import *
import sys

# 服务器地址
ADDR = ('127.0.0.1', 8888)


# 具体的请求功能
class FTPclient:
    pass

    def do_list(self):
        pass

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfe.close()
        sys.exit("谢谢使用！")

    def do_put(self):
        do_put


# 创建网络客户端
def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    while True:
        print("\n =========Command======== ")
        print(" ========= list ======== ")
        print(" ========= get_file ======== ")
        print(" ========= put_file ======== ")
        print(" ========= quit ======== ")
        print(" ========================= ")

        cmd = input(">>>>>>")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        else:
            print("请输入正确的命令！！！")
            s.send(cmd.encode())
            s.do_put()


#

if __name__ == '__main__':
    main()
