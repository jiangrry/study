[toc]

# 正则

## 1、正则表达式概述

### 1.1、简介、动机

现如今文本处理已经成文计算机的主要工作之一。文字处理、网页填表、数据库的信息流处理等等。因为我们可能不知道这些需要计算机编程处理文本或数据的具体内容，所以能把这些文本或数据以某种可被计算机识别和处理的模式表达出来是非常有用的。而正则表达式正是处理文本的解决方案，它是可以匹配文本片段的一种模式。

正则表达式(RE)为高级文本模式匹配，以及搜索###替代等功能提供了基础。正则表达式(RE)是一些由字符和特殊符号组成的字符串，它们描述了这些字符和字符的某种重复方式，因此能按某种模式匹配一个有相似特征的字符串的集合。

### 1.2、应用场景和解决问题

通过编程使计算机具有在文本中检索某种模式的能力
正则表达式为高级的文本模式匹配、抽取、或文本形式的搜索和替换功能提供基础
regex是一些由字符和特殊符号组成的字符串，它们描述了模式的重复或表述多个字符，于是regex能按照某种模式匹配一系列有相似特征的字符串
多种语言都提供了正则表达式接口，可以通过编程方便地处理正则表达式
regex的强大之处在于引入特殊字符来定义字符集、匹配自组和重复模式

## 2、元字符的使用

### 2.1、普通字符

匹配规则：每个普通字符匹配其对应的字符

```python
e.g.
In : re.findall('ab',"abcdefabcd")
Out: ['ab', 'ab']
```

> 注意：正则表达式在`python`中也可以匹配中文

###   2.2、元字符

#### 2.2.1、或关系

元字符: `|`

匹配规则: 匹配 `|` 两侧任意的正则表达式即可

```python
e.g.
In : re.findall('com|cn',"www.baidu.com/www.tmooc.cn")
Out: ['com', 'cn']
```

#### 2.2.2、匹配单个字符

元字符：`.`

匹配规则：匹配除换行外的任意一个字符

```python
e.g.
In : re.findall('张.丰',"张三丰,张四丰,张五丰")
Out: ['张三丰', '张四丰', '张五丰']
```

#### 2.2.3、匹配字符集

元字符： `[字符集]`

匹配规则: 匹配字符集中的任意一个字符

表达形式:

>   `[abc#!好]` 表示 `[] `中的任意一个字符
>   `[0###9],[a###z],[A###Z]` 表示区间内的任意一个字符
>   `[_#?0###9a###z]` 混合书写，一般区间表达写在后面

```python
e.g.
In : re.findall('[aeiou]',"How are you!")
Out: ['o', 'a', 'e', 'o', 'u']
```

#### 2.2.4、匹配字符集反集

元字符：`[^字符集]`

匹配规则：匹配除了字符集以外的任意一个字符

```python
e.g.
In : re.findall('[^0-9]',"Use 007 port")
Out: ['U', 's', 'e', ' ', ' ', 'p', 'o', 'r', 't']
```

#### 2.2.5、匹配字符串开始位置

元字符: `^`

匹配规则：匹配目标字符串的开头位置

```python
e.g.
In : re.findall('^Jame',"Jame,hello")
Out: ['Jame']
```

#### 2.2.6、匹配字符串的结束位置

元字符: `$`

匹配规则: 匹配目标字符串的结尾位置

```python
e.g.
In : re.findall('Jame$',"Hi,Jame")
Out: ['Jame']
```

>   规则技巧: `^` 和`$`必然出现在正则表达式的开头和结尾处。如果两者同时出现，则中间的部分必须匹配整个目标字符串的全部内容。

---

###   2.3、匹配字符重复

#### 2.3.1、元字符: `*`

匹配规则：匹配前面的字符出现0次或多次

```python
e.g.
In : re.findall('wo*',"wooooo~~w!")
Out: ['wooooo', 'w']
```

#### 2.3.2、元字符：`+`

匹配规则： 匹配前面的字符出现1次或多次

```python
e.g.
In : re.findall('[A-Z][a-z]+',"Hello World")
Out: ['Hello', 'World']
```

#### 2.3.3、元字符：`?`

匹配规则： 匹配前面的字符出现`0`次或`1`次

```python
e.g. 匹配整数
In [28]: re.findall('-?[0-9]+',"Jame,age:18,-26")
Out[28]: ['18', '-26']
```

#### 2.3.4、元字符：`{n}`

匹配规则： 匹配前面的字符出现`n`次

```python
e.g. 匹配手机号码
In : re.findall('1[0-9]{10}',"Jame:13886495728")
Out: ['13886495728']
```

#### 2.3.5、元字符：`{m,n}`

匹配规则： 匹配前面的字符出现`m-n`次

```python
e.g. 匹配qq号
In : re.findall('[1-9][0-9]{5,10}',"Baron:1259296994") 
Out: ['1259296994']
```

### 2.4、匹配任意字符

#### 2.4.1、匹配任意（非）数字字符

元字符： `\d` `\D`

匹配规则：`\d` 匹配任意数字字符，`\D` 匹配任意非数字字符

```python
e.g. 匹配端口
In : re.findall('\d{1,5}',"Mysql: 3306, http:80")
Out: ['3306', '80']
```

#### 2.4.2、匹配任意（非）普通字符

元字符： `\w` `\W`

匹配规则: `\w` 匹配普通字符，`\W` 匹配非普通字符

说明: 普通字符指数字，字母，下划线，汉字。

```python
e.g.
In : re.findall('\w+',"server_port = 8888")
Out: ['server_port', '8888']
```

#### 2.4.3、匹配任意（非）空字符

元字符： `\s` `\S`

匹配规则:`\s`匹配空字符，`\S` 匹配非空字符

说明：空字符指 空格`\r \n \t \v \f` 字符

```python
e.g.
In : re.findall('\w+\s+\w+',"hello    world")
Out: ['hello    world']
```

#### 2.4.4、匹配（非）单词的边界位置

元字符：`\b` `\B`

匹配规则：`\b` 表示单词边界，`\B` 表示非单词边界

说明：单词边界指数字字母(汉字)下划线与其他字符的交界位置。

```python
e.g.
In : re.findall(r'\bis\b',"This is a test.")
Out: ['is']
```

>   注意： 当元字符符号与`Python`字符串中转义字符冲突的情况则需要使用`r`将正则表达式字符串声明为原始字符串，如果不确定那些是`Python`字符串的转义字符，则可以在所有正则表达式前加r。

### 2.5、元字符小结

| 元字符   | 关系                        |
| -------- | --------------------------- |
| `｜`     | 或关系                      |
| `.`      | 匹配单个字符                |
| `[]`     | 匹配字符集                  |
| `[^]`    | 匹配字符集反集              |
| `^`      | 匹配字符串开始位置          |
| `$`      | 匹配字符串结束位置          |
| `*`      | 匹配前面的字符出现0次或多次 |
| `+`      | 匹配前面的字符出现1次或多次 |
| `?`      | 匹配前面的字符出现0次或1次  |
| `{n}`    | 匹配前面的字符出现n次       |
| `{n ,m}` | 匹配前面的字符出现n-m次     |
| `\d`     | 匹配任意数字字符            |
| `\D`     | 匹配任意非数字字符          |
| `\w`     | 匹配普通字符                |
| `\W`     | 匹配非普通字符              |
| `\s`     | 匹配空字符                  |
| `\S`     | 匹配非空字符                |
| `\b`     | 表示单词边界                |
| `\B`     | 表示非单词边界              |

### 案例一：正则表达式匹配

1.  匹配一个邮箱格式的字符串
2.  获取大写字母开头的单词：`Hello I A CBD iPython(不算)`

## 3、正则匹配规则

### 3.1、转义字符

#### 3.1.1、需要转义的字符

正则表达式用反斜杠字符`("\")` 来表示特殊格式或允许使用特殊字符而不调用它的特殊用法。正则表达式的特殊符号：`.  *  ?  $  ''  ""  []  {}  ()  \  ^`

例如匹配特殊字符 `.` 时使用`\.` 表示本身含义：

```python
In:  re.findall('-?\d+\.?\d*', "123, -123, 1.23, -1.23")
Out: ["123", "-123", "1.23", "-1.23"]
```

#### 3.1.2、`raw` 字符串

`raw `字串称为原始字符串。在`python`中在普通字串前加r即可，如：`r"hello world"`。原始字符串最大的特点是不会对字符串进行转义。

在`RE`中反斜杠的这个重复特性会导致大量重复的反斜杠，而且所生成的字符串也很难懂。解决的办法就是为正则表达式使用 `Python` 的 `raw `字符串表示；在字符串前加个`"r"` 反斜杠就不会被任何特殊方式处理，所以` r"\n"` 就是包含`"\"`和`"n"`的两个字符，而`"\n"`则是一个字符，表示一个换行。正则表达式通常在 `Python` 代码中都是用这种 `raw `字符串表示。

### 3.2、贪婪模式和非贪婪模式

#### 3.2.1、贪婪模式: 

默认情况下，匹配重复的元字符总是尽可能多的向后匹配内容。比如: `* + ? {m,n}`

#### 3.2.2、非贪婪模式(懒惰模式): 

让匹配重复的元字符尽可能少的向后匹配内容。

#### 3.2.3、贪婪模式转换为非贪婪模式

贪婪模式转换为非贪婪模式在匹配重复的元字符后加 `'?' `号即可

```python
*  :  *?
+  :  +?
?  :  ??
{m,n} : {m,n}?
    
e.g.
In : re.findall(r'\(.+?\)',"(abcd)efgh(higk)")
Out: ['(abcd)', '(higk)']
```

### 3.3、正则表达式分组

#### 3.1、分组

组是通过`"("` 和 `")"` 元祖符来标识的。`"("` 和 `")"` 有很多数学表达式相同的意思；它们一起把在它们里面的表达式组成一组。举例：你有用重复限制符，像`*, +, ? {m, n}`，来重复组里的内容，比如说：`(ab)*`将匹配零或更多个重复的`"ab"`。

子组的作用：

1.  子组可以改变重复元字符的操作对象；
2.  子组在某些操作中可以对子组匹配内容单独提取。

```PYTHON
In [5]: re.search('(ab)*', 'ababababab').group()
Out[5]: 'ababababab'

In [6]: re.search('王|李\w+', '李刚').group()
Out[6]: '李刚'

In [7]: re.search('王|李\w+', '王刚').group()
Out[7]: '王'

In [8]: re.search('(王|李)\w+', '王刚').group()
Out[8]: '王刚'
    
In [9]: re.search(r'http|https://\S+','http://www.baidu.com').group()
Out[9]: 'http'

In [10]: re.search(r'(http|https)://\S+','http://www.baidu.com').group()
Out[10]: 'http://www.baidu.com'

```

#### 3.2、捕获组和非捕获组

精心设计的`REs` 也许会用很多组，即可以捕获感兴趣的子串，又可以分组和结构化`RE` 本身。在复杂的`REs`里，追踪组号变得困难。开发人员的解决方法是使用`(?...)`来做为扩展语法。`Python` 新增了一个扩展语法到`Perl`扩展语法中。如果在问号后的第一个字符是`"P"`，你就可以知道它是针对`Python` 的扩展。目前有两个这样的扩展：`(?P<name>...)`定义一个命名组，`(?P=name)` 则是对命名组的逆向作用。

```PYTHON
In [11]: re.search(r'(?P<id>\d+)cdef', '123456cdefgh').group()
Out[11]: '123456cdef'

In [12]: re.search(r'(?P<id>\d+)cdef', '123456cdefgh').group('id')
Out[12]: '123456'

# (?P<捕获组名称>正则表达式)
In [13]: re.search(r'(?P<id>\d+)&(?P<name>\w+)ef', '123&李哲ef').group()
Out[13]: '123&李哲ef'

In [14]: re.search(r'(?P<id>\d+)&(?P<name>\w+)ef', '123&李哲ef').group('id')
Out[14]: '123'

In [15]: re.search(r'(?P<id>\d+)&(?P<name>\w+)ef', '123&李哲ef').group('name')
Out[15]: '李哲'

# 子组嵌套 由外向内数 由左向右
In [17]: re.search(r'(((?P<id>\d+)&)(?P<name>\w+))', '123&李哲').group()
Out[17]: '123&李哲'

# 第一组：(((?P<id>\d+)&)(?P<name>\w+))
# 第二组：(?P<id>\d+)
# 第三组：((?P<id>\d+)&)
# 第四组：(?P<name>\w+)
```

### 案例2：正则表达式匹配练习

1.  匹配一段文字中所有数字包含 整数 小数 正数 负数 百分数 
    分数 ` 12  1.6. 11.5. -5. 46.8% 1/3`
2.  匹配一个`IPV4`地址
3.  匹配一个身份证号

```python
# 1. 匹配数字
re.findall(r'-?\d+\.?/?\d*%?', '12 1.6 11.5 -5 46.8% 1/3')

# 2. IPV4 192.168.0.1
re.search(r'(\d{1,3}\.){3}\d{3}').group()

# 3. 身份证号
re.search(r'\d{17}(\d|x|X)', '11012019911230124X').group()
```

---

## 4、`Python RE` 模块使用

### 4.1、基础函数使用

```python
 regex = compile(pattern,flags = 0)
 功能: 
    生产正则表达式对象
 参数: 
    pattern  正则表达式
    flags  功能标志位,扩展正则表达式的匹配
 返回值: 
    正则表达式对象
```

```python
regex.findall(string,pos,endpos)
功能: 
	通过正则表达式匹配字符串
参数: 
	string  目标字符串
    pos  目标字符串的匹配开始位置
    endpos 目标字符串的结束位置
返回值: 
	匹配到的所有内容以列表返回
```

```python
regex.split(string)
功能: 
	按照正则表达式切割目标字符串
参数:
	目标字符串
返回值: 
	切割后的内容
```

```python
regex.sub（replaceStr，string，max）
功能： 
	替换正则表达式匹配到的内容
参数： 
	replaceStr 要替换的内容 
    string  目标字符串
    max   最多替换几处
返回值:
	返回替换后的字符串
```

```python
regex.subn（repl，string，count）
功能:
	替换正则表达式匹配到的内容
参数: 
	repl 要替换的内容 
    string  目标字符串
    count   最多替换几处
返回值: 
	返回替换后的字符串和实际替换的个数
```

```python
regex.finditer(string)
功能:
	使用正则表达式匹配目标内容
参数:
    目标字符串
返回值:
	迭代对象 迭代的每个内容为一个match对象

```

```python
regex.match(string)
功能:
    匹配一个字符串的开头
参数:
    目标字符串
返回值:
    如果匹配到返回 match obj，没有匹配到返回 None
```

```python
regex.search(string)
功能:
    匹配一个字符串
参数:
    目标字符串
返回值:
    如果匹配到返回 match obj，没有匹配到返回 None
```

```python
regex.fullmatch(string)
功能:
    完全匹配一个字符串
参数:
    目标字符串
返回值:
    如果匹配到返回 match obj，没有匹配到返回 None
```

---

### 4.2、 `compile` 对象

#### 4.2.1、`compile` 对象方法

在`re`模块中可以直接调用一些正则表达式操作函数，而这些函数也可以使用`compile`函数返回值对象来调用，只是被`re`调用时第一个参数为`pattern`，被`compile`对象调用时第一个不用加`pattern，flags`，同时增加了`pos，endpos`参数。因为已经在调用`compile`函数时声明了`pattern，flags`。所以功能是一样的。

#### 4.2.2、 `compile` 对象属性

`compile `对象除了有很多匹配函数之外还有些特有的属性
如下:

-   `flags `: 标志位
-   `pattern`:  正则表达式
-   `groupindex` : 捕获组形成的字典
-   `groups`: 多少个子组

### 4.3、`match` 对象属性

```python
# 属性变量： 
match_obj.pos   # 目标字符串开头位置
match_obj.endpos   # 目标字符串结束位置
match_obj.re   # 正则表达式对象
match_obj.string  # 目标字符串
match_obj.lastgroup   # 最后一组的名字
match_obj.lastindex   # 最后一组是第几组

# 属性方法
span()   
	功能: 匹配到内容的起止位置
start() 
	功能: 匹配到内容的开始位置
end()  
	功能: 匹配到内容的结束位置
groups() 
	功能: 得到所有子组匹配的内容
groupdict() 
	功能: 得到所有捕获组匹配的内容

group(n)
功能:
    获取match 对象匹配的内容
参数:
    默认为0 表示获取正则整体的匹配内容
    如果传入大于0的正数则表示获取对应子组匹配内容
返回值:
    返回匹配到的内容

```

### 4.4、标志位

#### 4.4.1、`flags` 参数

`re`模块调用的匹配函数。如：`re.compile,re.findall..``.都有一个`flags`参数，用于扩展丰富正则表达式的匹配功能。
常用`flag：`

-   `A == ASCII ` 元字符只能匹配`ascii`码
-   `I == IGNORECASE`  匹配忽略字母大小写
-   `S == DOTALL`  使 `.` 可以匹配换行
-   `M == MULTILINE`  使`^ $` 可以匹配每一行的开头结尾位置

### 案例3：在文件中匹配地址

利用所给文件完成：编写一个函数，传入端口名称，返回这个端口运行情况中所表述的 `address` 地址信息。

提示：

-   每段之间有空行
-   每段单词是端口号
-   端口名可能很复杂

---

# 综合练习

## 案例4: 文件操作练习

```python
一个文件，文件名："talk.txt"。在文件中保存着一些对话信息，格式如下：
老王: 吃了吗
老李: 吃过了，您呐？
老王:  还没呢，刚买点菜
老张: 老哥俩干什么呢？
老李: 遛弯呗
老张: 买没少买
老王: 是啊，回家了，回见了您

通过程序将该文件进行分离，每个任务的说话内容，重新写入到一个新文件中，文件以这个人的名字命名。
```

## 案例5: 文件括号匹配验证

```python
用户可以根据 input() 选择一个文本文件 (存在大量的括号(),[],{},《》，但是这些括号可能存在匹配不正确的情况)，判断文件中扣号匹配是否正确，如果正确则回复完全正确的信息，如果不正确，需要告知提示不正确，并且指出括号不正确的位置。
```

## 案例6: 线程同步互斥

```python
写两个线程，一个线程打印 1-52，另一个线程打印 A-Z，要求打印顺序为 12A34B56C...5152Z，不能使用 sleep 进行时间控制。
```

## 案例7: 模拟窗口卖票

```python
有 10 个窗口 (w1...w10)，同时开放售票，一共有 50 张票(T1-T50)，需要按照顺序出售
要求：
	输出每一张票的出售时间和窗口，每张票的出票时间 0.1秒，不能出现票未出售或者出售多次的情况。窗口开放之前票存在容器中。
    1. 使用多线程的同步互斥方法解决问题输出结果
    2. 每个线程模拟售票情景
    3. 将票的存储提前定一个合理的结构
```

## 案例8: `MySQL` 练习

```python
根据给出的数据完成查找练习。
```

## 案例9: 正则表达式练习

```python
根据要求完成正则表达式匹配练习。
```

