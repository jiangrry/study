# 元字符
#### 1、匹配普通字符 （“|”）
    匹配规则：每个普通字符匹配对应其字符；正则表达式在Python中也能够匹配中文。
    in:re.findall('A|B',example)
    out：['A','B']


#### 2、匹配单个字符 （“.”）
    匹配规则：匹配除了换行外的任意一个字符。


#### 3、匹配字符集 []
    匹配规则：匹配字符集中的任意一个字符。
    表达形式：[abc#!好] 表示的时[]中的任意一个字符；
           [0-9],[a-z],[A-Z] 表示的是区间内部的任意一个字符；
           [_#?0-9a-z] 混合书写，一般区间表示在后面


#### 4、字符集取反 [^字符集]
    匹配规则：匹配除了字符之外的任意一个字符。   
    表达形式：[^字符集]；


#### 5、匹配字符串开始位置^ 
    - 匹配规则：匹配目标字符串开头的位置
    - 表达形式：^     


#### 6、匹配字符串结尾位置 $
    - 匹配规则：匹配目标字符串结尾的位置
    - 表达形式：$

    <br/>
    _规则技巧：^和$ 必然会出现在正则表达式的开头和结尾。
    若两者同时出现，则中间的部分必须匹配整个目标字符串的全部内容。_

#### 7.1、匹配字符重复*
    - 匹配规则：匹配前面的字符出现的0次或者多次
    - 表达形式：*


#### 7.2、匹配字符重复+
    - 匹配规则：匹配前面的字符出现的1次或者多次
    - 表达形式：+


#### 7.3、匹配字符重复？
    - 匹配规则：匹配前面的字符出现的0次或者1次
    - 表达形式：？
    # 匹配整数
    print(re.findall('-?[0-9]+','2020年8月13日 20时55分')) 
        >>>> ['2020', '8', '13', '20', '55']

#### 7.4、匹配字符重复{n}
    - 匹配规则：匹配前面的字符出现的n次
    - 表达形式：{n}
    print(re.findall('ab{3}','abbbbbbbbbbbb')) >>>> ['abbb']

#### 7.5、匹配字符重复{m,n}
    - 匹配规则：匹配前面的字符出现的m-n次
    - 表达形式：{m,n}
    print(re.findall('[1-9][0-9]{4,10}','likia:104553697'))
        >>>> ['104553697']


#### 8、匹配（非）数字字符 \d；\D
    - 匹配规则：\d 匹配任意数字字符；\D 匹配任意非数字字符
    - 表达形式：\d；\D
    print(re.findall('\d+','port:3306')) >>>> ['3306']


#### 9、匹配（非）普通字符 \w；\W
    - 匹配规则：\w 匹配任意普通字符；\W 匹配任意非普通字符
    _说明：普通字符指的是数字，字母，下划线，汉字_
    - 表达形式：\w；\W

#### 10、匹配（非）空字符 \s；\S
    - 匹配规则：\s 匹配空字符；\S 匹配非空字符
    _说明：空字符指的是 空格、\r、\n、\t、\v、\f、字符_
    - 表达形式：\s；\S

#### 11、匹配（非）单词边界位置 \b；\B
    - 匹配规则：\b 匹配单词边界；\B 匹配非单词便捷
    _说明：单词便捷指数字字母（汉字）下划线与其他字符的交界位置_
    - 表达形式：\b；\B
    注意：当元字符符号与python字符串中转义字符冲突的情况则需要使
         用r将正则表达式声明为原始字符串

### 转义字符

    _非贪婪模式（懒惰模式）：让匹配重复的元字符尽可能少的向后匹配内容；_
    _贪婪模式：在非贪婪模式的基础上再匹配重复的元字符后面加上'?'号即可_

### re 模块下的函数（RE模块函数用法 ）
```python
import re 
re.findall() # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
             # re.findall(pattern, string, flags=0)或pattern.findall(string[, pos[, endpos]])
             # string:目标字符串;pos:目标字符串匹配开始的位置;endpos:目标字符串的结束位置
             # 返回值:匹配到所有的内容以列表的形式返回   

re.split() 
# split 方法按照能够匹配的子串将字符串分割后返回列表.
# re.split(pattern, string[, maxsplit=0, flags=0])
l = 'Are you Ok aa!!'
l2 = re.split('[^\w]', l)
print(l2)
# ['Are', 'you', 'Ok', 'aa', '', '']

re.compile(pattern,flags = 0) 
# pattern:正则表达式;
# flags:功能位置,提供更为丰富的匹配,默认值等于的情况下,不加以赋值;
# 返回值：正则表达式对象
l = 'Are you Ok aa!!'
pattern = r'[a-z]'
print(re.findall(pattern,l,flags=0))
# ['r', 'e', 'y', 'o', 'u', 'k', 'a', 'a']

re.sub(replaceStr,string,max)
# 功能:替换正则表达式匹配到的内容
# 参数:replaceStr是要替换的内容;string是目标字符串;max是最多可替换几处
# 返回值:返回替换后的字符串
l1 = 'Are you Ok aa!!'
print(re.sub(r' ','--',l1)) # >>> Are--you--Ok--aa!!
print(re.sub(r' ','--',l1,2)) # >>> Are--you--Ok aa!!

re.finditer(pattern,string)
# 功能:使用正则表达式匹配目标内容
# 参数:目标字符串
# 返回值:迭代目标，迭代的每一个内容为一个match对象
# 匹配目标字符串得到迭代对象
# 可以使用print(i.group())获取迭代休想内容
s2 = '1994,04,2 2,29s44,sdfff,sdf '

item = re.finditer(r'\s+', s2)
for i in item:
    print(i)
# <re.Match object; span=(9, 10), match=' '>
# <re.Match object; span=(27, 28), match=' '>

re.match(pattern,string)
# 功能:匹配一个字符串的开头
# 参数:目标字符串
# 返回值:如果匹配则返回match.obj,如果没有则返回到匹配None
# match对象的group(n)
    # 功能:获取match对象匹配内容
    # 参数:默认为零,表示获取正则表达式的整体匹配内容，如果传值大于零，则表示匹配对应子组内容
    # 返回值:返回匹配到的内容
s2 = '1994,04,2 2,29s44,sdfff,sdf '
print(re.match(r'\d+',s2))
# <re.Match object; span=(0, 4), match='1994'>
s2 = '   1994,04,2 2,29s44,sdfff,sdf '
print(re.match(r'\d+',s2))
# None

re.search(pattern,string)
# 功能:匹配一个字符串
# 参数:目标字符串
# 返回值:如果匹配则返回match.obj,如果没有则返回到匹配None
s2 = '1994,04,2 2,29s44,sdfff,sdf '
print(re.search(r'\d+',s2))
s2 = '   1994,04,2 2,29s44,sdfff,sdf '
print(re.search(r'\d+',s2))
# <re.Match object; span=(0, 4), match='1994'>
In [11]: re.search(r'(?P<id>\d+)cdef', '123456cdefgh').group()
Out[11]: '123456cdef'

In [12]: re.search(r'(?P<id>\d+)cdef', '123456cdefgh').group('id')
Out[12]: '123456'



re.fullmatch(pattern,string)
# 功能:完全匹配一个字符串
# 参数:目标字符串
# 返回值:如果匹配则返回match.obj,如果没有则返回到匹配None
s2 = '1994,04,2 2,29s44,sdfff,sdf '
print(re.fullmatch(r'.+',s2))
# <re.Match object; span=(0, 28), match='1994,04,2 2,29s44,sdfff,sdf '>
```

## 正则匹配规则



### 常见面试题
