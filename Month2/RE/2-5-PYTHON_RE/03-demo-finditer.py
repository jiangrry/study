"""
    finditer 演示
"""
import re

s = "1949年10月1日，中华人民共和国成立"

# re 模块使用 finditer
it = re.finditer(r'\d+', s)
for i in it:
    print(i.group())

# compile 对象调用 finditer
regex = re.compile(r'\d+')
item = regex.finditer(s)
for i in item:
    print(i.group())
