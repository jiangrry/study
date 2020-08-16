"""
    flags 功能标志位演示
"""

import re

s = """Hello
北京
"""
regex = re.compile(r'\w+')
res = regex.findall(s)
print(res)

# 1. re.A 只匹配 ascii 编码
regex = re.compile(r'\w+', flags=re.A)
res = regex.findall(s)
print(res) # ['Hello']

# 2. re.I 忽略大小写
regex = re.compile(r'[a-z]+', flags=re.I)
res = regex.findall(s)
print(res) # ['Hello']

# 3. re.S --> 在匹配过程中 可以让 . 匹配到换行
# regex = re.compile(r'.+')
regex = re.compile(r'.+', flags=re.S)
res = regex.findall(s)
print(res) # ['Hello\n北京\n']

# 4. re.M --> 表示可以匹配到每一行的开头和结尾
regex = re.compile(r'^北京+',flags=re.M | re.I)
res = regex.findall(s)
print(res) # ['Hello\n北京\n']