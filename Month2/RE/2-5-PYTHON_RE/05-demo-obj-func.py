"""
    compile 调用
        match 只匹配开头位置
        search 只匹配第一个
        fullmatch 完全匹配
"""
import re

s = " 1949年10月1日，中华人民共和国成立"
obj = re.compile(r'\d+')
# match
res = obj.match(s)
print(res)

# search
res = obj.search(s)
print(res)

res = obj.fullmatch(s)
print(res)