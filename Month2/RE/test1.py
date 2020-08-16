# -*- coding:utf-8 -*-
# email:jiangrry@qq.com
# author:jiangrry

import re

s = "因获得《雅虎搜星》比赛冯小刚组冠军而进入演艺圈 [1]  ；同年，在冯小刚执导的广告片《跪族篇》中担任女主角 [2]  。2011年，因在古装剧《新还珠格格》中饰演晴儿一角而被观众认识 [3] "
l = 'Are you Ok aa!!'
j = '2020年8月13日 20时55分'

# print(re.findall(r"《\w+》", s))
# print(re.findall('在',s))
# print(re.findall('[a-z]',l))
# print(re.findall('[A-Z]',l))
# print(re.findall('[a-zA-Z]',l))
# print(re.findall('[^a-zA-Z]',l))


# print(re.findall('[a-z*]',l))
# print(re.findall('[A-Z+]',l))

# print(re.findall('-?[0-9]+',j))
# print(re.findall('-?[0-9]+','2020年8月13日 20时55分'))
# print(re.findall('ab{3}','abbbbbbbbbbbb'))
# print(re.findall('[1-9][0-9]{4,10}','likia:104553697'))

# print(re.findall('\d+','port:3306'))

# 使用指定字符串替换匹配到的内容

# l1 = 'Are you Ok aa!!'
# print(re.sub(r' ','--',l1))
# print(re.sub(r' ','--',l1,2))

# pattern = r'[a-z]+'
# print(re.findall(pattern,l,flags=0))

# l2 = re.split('[^\w]', l)
# print(l2)

# 匹配目标字符串得到迭代对象
# s2 = '1994,04,2 2,29s44,sdfff,sdf '

# item = re.finditer(r'\d+', s2)
# for i in item:
#     print(i.group())

# print(re.match(r'\d+',s2))

# print(re.search(r'\d+',s2))

# print(re.fullmatch(r'.+',s2))


### 正则表达式匹配练习

"""
1.  匹配一段文字中所有数字包含 整数 小数 正数 负数 百分数 
    分数 ` 12  1.6. 11.5. -5. 46.8% 1/3`
2.  匹配一个`IPV4`地址
3.  匹配一个身份证号
"""

import re

score = '12  1.6. 11.5. -5. 46.8% 1/3'
print(re.findall(r'-?\d+\.?/?\d*%?', '12  1.6. 11.5. -5. 46.8% 1/3'))

print(re.search(r'', '330724199404221317').group())

# c = re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))\.){3}((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))$')
# ip = input("请输入一个ip地址：")
#
# s = c.search(ip)
# if s:
#     print(s.group())
