# -*- coding: UTF-8 -*- 
# author(作者):jiangrry

from socket import *


def find_word(data):
    """

    :param data: 查找的单词
    :return:
    """

    f = open("dict.txt")
    for line in f:
        w = line.split(" ")[0]
        if w > data:
            f.close()
            return "没有找到该单词"
        elif w == data:
            f.close()
            return line
    else:
        f.close()
        return "没有找到该单词"


sockdf = socket(AF_INET, SOCK_DGRAM)

sockdf.bind(("127.0.0.1", 8888))

while True:
    data, addr = sockdf.recvfrom(1024)
    result = find_word(data.decode())
    sockdf.sendto(result.encode(), addr)

sockdf.close()
