# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry

"""
    event 互斥方法
        引入
"""

from threading import Event, Thread
from time import sleep

e = Event() # 创建 Event 对象
s = None  # 全局变量 --> 用于通信 共享资源


def func01():
    print("对口令！！！")
    global s
    s = "天王盖地虎"
    e.set() # 终止阻塞


t = Thread(target=func01)
t.start()
print("对对口令才是自己人")
e.wait() # 主线程会阻塞等待
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("自己人")
else:
    print("开枪，打死你！")
