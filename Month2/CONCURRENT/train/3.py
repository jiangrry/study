# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry
import socket
import re
from select import *
from multiprocessing import Process

# 设置html文件地址
HTML_ROOT_DIR = "defult.html"


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
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.server_socket.listen(10)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s %s]用户连接上了" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
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
            file_name = "defult.html"

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
        self.bind(self.address)

        # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        # IO多路复用接收客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs, wx, xs = select(self.rlist,
                                self.wlist,
                                self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:
                    # 处理请求
                    self.handle(r)



def main():
    http_server = HttpServer()
    http_server.bind()
    http_server.start()


if __name__ == "__main__":
    main()