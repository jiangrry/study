# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry

"""
使用进程池拷贝一个目录及目录中所有内容
	- 目录中的内容均为普通文件
    - 进程池中执行的每个进程事件拷贝一个文件
    - 实时显示拷贝的百分比
"""

# 拷贝文件路径
# 存放目标位置
# 确定文件大小
# 创建进程池
# 复制文件
# 显示拷贝百分比

import os
from multiprocessing import Pool, Queue

q = Queue()


def copy_file(file, old_folder, new_folder):
    """
    复制文件
    :param file: 文件名称
    :param old_folder: 原始路径
    :param new_folder: 新路径
    :return:
    """
    fr = open(old_folder + '/' + file, 'rb')
    fw = open(new_folder + '/' + file, "wb")
    while True:
        data = fr.read(1024 * 1024)
        if not data:
            break
        n = fw.write(data)
        q.put(n)
    fr.close()
    fw.close()


def main():
    # 拷贝文件路径
    base_path = r"G:/"
    dir = input("输入你要拷贝的路径")
    old_folder = base_path + dir
    # 存放目标位置
    new_folder = old_folder + "-back"
    os.mkdir(new_folder)
    # 确定文件大小
    all_file = os.listdir(old_folder)
    total_size = 0
    for file in all_file:
        total_size += os.path.getsize(old_folder + '/' + file)
    # 创建进程池
    pool = Pool()
    for file in all_file:
        pool.apply_async(func=copy_file, args=(file, old_folder, new_folder))
    pool.close()
    # 复制文件
    print("目录大小:%.2fM" % (total_size / 1024 / 1024))
    copy_size = 0
    while True:
        copy_size += q.get()
        print("拷贝了 %.1f%%" % (copy_size / total_size * 100))
        if copy_size >= total_size:
            break
    pool.join()


main()
# 显示拷贝百分比

# def objFileName():
#     fileNameList = r"G:\dict.txt"
#     objNameList = []
#     for i in open(fileNameList, 'r'):
#         objNameList.append(i.replace('\n', ''))
#     return objNameList
