# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry


from socket import *
from select import *


class HttpServer(object):
    def __init__(self, host='127.0.0.1', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 实例化对象时直接创建套接字
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # self.sockfd.setblocking(False)

    def bind(self):
        self.sockfd.bind((self.address))

    def start_server(self):
        self.sockfd.listen(10)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        while True:
            rs, wx, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect form", addr)
                    self.rlist.append(c)
                else:
                    self.handle(r)

    def handle(self, connfd):
        request = connfd.recv(4096)
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print("请求内容：", info)

        if info == "/" or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

    def get_html(self, connfd, info):
        if info == '/':
            filename = self.dir + "/defult.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry....</h1>'
        else:
            # 网页存在：
            response = "HTTP/1.1 2OO OK\r\n"
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += fd.read()
        finally:
            connfd.send(response.encode())

    def get_data(self, connfd, info):
        response = "HTTP/1.1 404 Not Found\r\n"
        response += 'Content-Type:text/html\r\n'
        response += '\r\n'
        response += '<h1>Sorry....</h1>'


if __name__ == '__main__':
    # 用户的参数
    HOST = '127.0.0.1'
    PORT = 8000
    DIR = 'G:\Study\\NOTE\Month2\CONCURRENT\train\static'

    httpd = HttpServer(HOST, PORT, DIR)
    httpd.start_server()
