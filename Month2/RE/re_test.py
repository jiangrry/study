# -*- coding:utf-8 -*-
# author:jiangrry

import re

# 匹配一个邮箱格式的字符串
res1 = re.findall(r'\w+@\w+\.com|\w+@\w+\.cn', "jiangrry@qq.com")
print(res1)
print( re.findall(r'\w+@\w+\.com|\w+@\w+\.cn', "jiangrry@qq.com"))


# 获取大写字母开头单词

res2 = re.findall(r'\b[A-Z]\w*',"Hello,I,A,CBD,iPYTHON")
print(res2)


# 匹配一个IP地址
