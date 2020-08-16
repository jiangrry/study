# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry


# with lock： 默认缩进
#   print ("HELLO")


from threading import Lock, Thread

lock = Lock()
a = b = 0


# 线程函数

def value():  # 分支线程
    while True:
        lock.acquire()  # 加锁
        if a != b:
            print("a = %d,b =%d " % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    with lock: # with代码块结束后会自动解锁
        a += 1
        b += 1

t.join()
