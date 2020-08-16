"""
    compile 对象属性演示
"""
import re

regex = re.compile(r'\d+')

print(regex.pattern)

print(regex.flags)
regex = re.compile(r'\d+', re.I)
print(regex.flags)

regex = re.compile(r'(?P<id>\d+)ab(cd)', re.I)
print(regex.groups)

print(regex.groupindex)

regex = re.compile(r'(((?P<id>\d+)&)(?P<name>\w+))')
print(regex.groupindex)