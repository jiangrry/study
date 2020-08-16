"""
    match 对象 演示
"""
import re

regex = re.compile(r'(ab)cd(?P<id>\d+)')
obj = regex.search('abcd123456asasasa', 0, 10)
print(obj)  # <_sre.SRE_Match object; span=(0, 10), match='abcd123456'>

# 属性
print('正则表达式：', obj.re)
print('目标字符串：', obj.string)
print('起始位置：', obj.pos)
print('终止位置：', obj.endpos)
print('最后一组组名：', obj.lastgroup)
print('最后一组组号：', obj.lastindex)

# 属性方法
print('匹配内容的位置：', obj.span(), obj.start(), obj.end())
print('获取子组内容：', obj.groups())
print('获取捕获组内容:', obj.groupdict())
print('对应内容：', obj.group())
print('对应内容：', obj.group('id'))
print('对应内容：', obj.group(1))
