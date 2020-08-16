# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry

"""
HTTPServer
功能
1.  接收客户端的HTTP请求
2.  对请求有一定的解析
3.  根据请求内容组织响应
4.  将响应内容返回给客户端
特点
-   使用多路复用完成并发接收
-   使用类进程封装
-   能够根据具体请求返回指定的网页
"""
from socket import *
from select import *
import re

HTML_ROOT_DIR = './static'

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
        self.sockfd = socket(AF_INET, SOCK_STREAM)
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        # IO多路复用接收客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs, wx, xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:
                    # 处理请求
                    self.handle_client(r)

    def handle_client(self,client_socket):
        """处理客户端请求"""
        # 获取用户端请求
        request_data = client_socket.recv(1024)
        print("request_data:", request_data)
        request_lines = request_data.splitlines()
        # 请求解析
        request_start_line = request_lines[0]
        # 获取用户请求的文件名
        file_name = re.match(r"\w+ +(/[^ ]*)", request_start_line.decode('utf-8')).group(1)

        if "/" == file_name:
            file_name = "./static"

        # 打开文件，阅读内容
        try:
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found!"

        else:
            file_data = file.read()
            file.close()

            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            response_body = file_data.decode("utf-8")

        response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)

        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))

        # 关闭客户端连接
        client_socket.close()

    def bind(self):
        self.sockfd.bind((self.address))


# 用户使用HTTPServer
if __name__ == "__main__":
    """
    通过 HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = '127.0.0.1'
    PORT = 8000
    DIR = "./static"  # 网页存储位置

    httpd = HttpServer(HOST, PORT, DIR)  # 实例化对象
    httpd.start()  # 启动服务
# def main():
#     http_server = HttpServer()
#     http_server.bind()
#     http_server.start()
#
#
# if __name__ == "__main__":
#     main()