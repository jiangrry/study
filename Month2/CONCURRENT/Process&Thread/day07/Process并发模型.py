# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry


"""
    基于　Process 多进程并发
"""
from socket import *
from multiprocessing import Process
import os
import signal

ADDR = ('0.0.0.0', 8888)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(10)
signal.signal(signal.SIGHUP, signal.SIG_IGN)
print("Listen port 8888....")


def handld(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


while True:
    try:
        c, addr = s.accept()
        print("Content from: ", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    p = Process(target=handld, args=(c,))
    p.daemon = True
    p.start()




# """
#     多线程并发
# """
# import os
# from threading import Thread
# from socket import *
#
# # 全局变量
# ADDR = ('0.0.0.0', 8888)
#
#
# def handle(c):
#     """
#         分支线程处理客户端请求
#     :param c:　处理与客户端请求的套接字对象
#     """
#     while True:
#         data = c.recv(1024)
#         if not data:
#             break
#         print(data.decode())
#         c.send(b"OK")
#     c.close()
#
#
# # 创建套接字
# s = socket()
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
# s.bind(ADDR)
# s.listen(10)
# print("Listen port 8888...")
#
# while True:
#     try:
#         c, addr = s.accept()
#         print("Content from:", addr)
#     except KeyboardInterrupt:
#         s.close()
#         os._exit(0)
#     except Exception as e:
#         print(e)
#     # 创建线程处理客户端请求
#     t = Thread(target=handle, args=(c,))
#     t.setDaemon(True)
#     t.start()