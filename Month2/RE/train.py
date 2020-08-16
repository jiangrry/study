# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry

import os
import io
import re


def get_address(port):
    """

    :param port: 对应的端口名称
    :return: 输入的端口返回的address
    """
    f = open('exc.txt')
    while True:
        data = ""
        for line in f:
            if line == '\n':
                break
            data += line
        if not data:
            return "没有该端口信息!!"
        object = re.match(r'\S+', data)
        if port == object.group():
            pattern = r'(\d{1,3}\.){3}\d{1,3}/\d{2}|unknown'
            object = re.search(pattern, data)
            if object:
                return object.group()


if __name__ == '__main__':
    port = input("端口号:")
    print(get_address(port))
