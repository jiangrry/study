# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry


"""
    多线程
"""
from threading import Thread
from time import sleep


def music(sec, name):
    sleep(sec)
    print("播放 %s" % name)


list01 = ["少年", "信仰", "泡沫"]
jobs = []
for i in list01:
    th = Thread(target=music, args=(2, i))
    jobs.append(th)
    th.start()
for i in jobs:
    i.join()
