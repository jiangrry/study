"""
    re 模块调用函数
        findall： 只要有子组，他会返回自足对应的内容
"""
import re

s = "Alex:1990,Tom:1998"
pattern = r'\w+:\d+'
# 1.1. re直接调用 findall
result = re.findall(pattern, s)
print(result)  # ['Alex:1990', 'Tom:1998']

# 1.2. re直接调用 findall --> 加上子组
pattern = r'(\w+):\d+'
result = re.findall(pattern, s)
print(result)  # ['Alex', 'Tom']

# 1.3. re直接调用 findall --> 加上两个子组
pattern = r'(\w+):(\d+)'
result = re.findall(pattern, s)
print(result)  # [('Alex', '1990'), ('Tom', '1998')]

# 2. split()
result = re.split(r'[^\w]', s)
print(result)  # ['Alex', '1990', 'Tom', '1998']

# 3. sub
# result = re.sub(r':', '--', s, 1)
# print(result)  # Alex--1990,Tom:1998

# 4. subn
result = re.subn(r':', '--', s)
print(result)  # ('Alex--1990,Tom--1998', 2)
