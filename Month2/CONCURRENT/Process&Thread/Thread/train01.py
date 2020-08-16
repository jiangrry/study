# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry


"""
使用多个线程从不同的地方拷贝一个文件，每个线程负责拷贝文件的一部分
"""
"""
    使用多个线程从不同的地方拷贝一个文件，
    每个线程负责拷贝文件的一部分
    问题：
        多个线程到底是几个？
        多个线程写入同一个文件中如何确定位置？
"""
from threading import Thread, Lock
import os

lock = Lock()
urls = [
    '/home/tarena/桌面/',
    '/home/tarena/文档/',
    '/home/tarena/下载/',
    '/home/tarena/音乐/',
    '/home/tarena/图片/',
    '/home/tarena/AIDVN2005/',
    '/home/tarena/',
]

filename = input("要下载的文件")

explorer = []  # 存放要下载文件所在的绝对路径

for i in urls:
    if os.path.exists(i + filename):  # /home/tarena/桌面/dict.txt
        explorer.append(i + filename)

path_num = len(explorer)
if path_num == 0:
    os._exit(0)  # 如果没有的话，下面不用执行

file_size = os.path.getsize(explorer[0])
block_size = file_size // path_num  # 每个线程下载多大
fd = open(filename, 'wb')


def load(path, num):
    """
        模拟下载
    :param path: 下载路径
    :param num: 下载多少 -->
    """
    f = open(path, 'rb')
    seek_num = block_size * num  # 向后移动多少 偏移量
    f.seek(seek_num)
    data = f.read(block_size)
    with lock:  # 加锁写入
        fd.seek(seek_num)
        fd.write(data)


num = 0
jobs = []
for path in explorer:
    t = Thread(target=load, args=(path, num))
    jobs.append(t)
    t.start()
    num += 1
for i in jobs:
    i.join()
