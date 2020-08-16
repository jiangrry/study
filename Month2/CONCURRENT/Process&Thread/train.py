# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry

# 分别求证使用4个进程和10个进程计算100000以内质数之和的时间，与单进程比较，看是否提高了运行效率
# 质数：只能被一和自身正数得数
# 不使用进程
# 使用四个进程
# 使用是个进程

import multiprocessing
import time
# 装饰器 ———> 本质就是闭包
# 函数嵌套；内部函数使用外部函数变量；外部函数返回值必须是内部函数

# 面试题
def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间：%.8f" % (f.__name__, end_time - start_time))
        return res

    return wrapper


def ifprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True


@timeit
def no_multi_process():
    prime = []
    for i in range(1, 100001):
        if ifprime(i):
            prime.append(i)
    sum(prime)


class prime2(multiprocessing.Process):
    def __init__(self, prime, begin, end):
        super().__init__()
        self.prime = prime
        self.begin = begin
        self.end = end

    def run(self):
        for i in range(self.begin, self.end):
            if ifprime(i):
                self.prime.append(i)
        sum(self.prime)


@timeit
def use_multi_process():
    prime = []
    processes = []
    for i in range(1, 100001, 25000):
        p = prime2(prime, i, i + 25000)
        p.start()
        processes.append(p)
    [process.join() for process in processes]


@timeit
def use10_multi_process():
    prime = []
    processes = []
    for i in range(1, 100001, 10000):
        f = prime2(prime, i, i + 10000)
        f.start()
        processes.append(f)
    [process.join() for process in processes]


if __name__ == '__main__':
    no_multi_process()
    use_multi_process()
    use10_multi_process()
