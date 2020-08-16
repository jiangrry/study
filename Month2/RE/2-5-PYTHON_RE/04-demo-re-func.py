"""
    re 调用
        match 只匹配开头位置
        search 只匹配第一个
        fullmatch 完全匹配
"""
import re

s = " 1949年10月1日，中华人民共和国成立"

# match 只匹配开头位置
result = re.match(r'\d+', s)
print(result)

# search
result = re.search(r'\d+', s)
print(result)

# fullmatch
result = re.fullmatch(r'\d+',s)
print(result)
result = re.fullmatch(r'.+',s)
print(result)