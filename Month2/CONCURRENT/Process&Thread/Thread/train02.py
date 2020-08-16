# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry
def count(x, y):
    """
        计算密集型程序
    """
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1
def write():
    """
        写
    """
    f = open("test.txt", 'w')
    for i in range(1800000):
        f.write("hello world\n")
    f.close()
def read():
    """
        读
    """
    f = open("test.txt")
    f.readline()
    f.close()
def io():
    """
        io 密集型
    """
    write()
    read()
