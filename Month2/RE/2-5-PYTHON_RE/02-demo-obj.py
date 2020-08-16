"""
    compile 对象调用
"""
import re

s = "Alex:1990,Tom:1998"
pattern = r'\w+:\d+'

# 创建 compile 对象
obj = re.compile(pattern)

# 1. 对象调用 findall
res = obj.findall(s, 0, 12)  # s[0:12]
print(res)  # ['Alex:1990']

# 2. split()
pattern = r'[^\w]'
obj = re.compile(pattern)
res = obj.split(s)
print(res)  # ['Alex', '1990', 'Tom', '1998']

# 3. sub
obj = re.compile(r':')
# res = obj.sub('==', s)
# print(res)  # Alex==1990,Tom==1998

# 4. subn
res = obj.subn('==', s)
print(res)  # ('Alex==1990,Tom==1998', 2)
