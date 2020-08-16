# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry


"""
编写一个服务端程序，
同时监控多个客户端发送过来的错误信息，将其写入到一个日志文件中。
同时监控服务端的本地输入内容，也写入到日志中。
日志内容包含信息和时间，每条占一行。
"""

from socket import *
from select import select
from time import ctime
import sys

# 创建全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(10)

f = open('log.txt', 'a')

rlist = [s, sys.stdin]
wlist = []
xlist = []
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            rlist.append(c)
        elif r is sys.stdin:  # 当有终端输入时，也要讲内容写入文件中
            f.write("%s %s" % (ctime(), r.readline()))
            f.flush()
        else:
            data = c.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            f.write("%s %s" % (ctime(), data.decode()))
            f.flush()
