1. 简单谈一下你对Python这门语言的理解

```
设计哲学：强调代码的可读性和简洁的语法
动态解释型语言，灵活，包容
强类型语言, '鸭子模型' 
应用领域：Web，爬虫，大数据，云计算，AI
跨平台-真正做到一处编写，到处执行
与Java、C、Go等语言对比优势和劣势
```



#### 2. Python2中文编码问题

```
Python2使用 ASCII 作为默认编码方式（历史原因）
Python3使用Unicode作为默认编码，str和bytes
```



#### 3. 谈一下List、Tuple、Set的区别和联系

```
都是可迭代集合对象，List、Tuple可以互相转换
List、Set可变，Tuple不可变
Set内对象不重复，可以用于语言级排重
Tuple性能略好
```



#### 4. 谈一下进程和线程的关系，什么时候用进程，什么时候用线程？

```
IO密集型 – 线程
CPU密集型 – 进程
```



#### 5. Python多线程编程

```python
threading模块
最基础的是start、join两个方法
锁：threading.Lock和threading.RLock

import threading, time

def doWaiting():
    print("start waiting", time.strftime("%H:%M:%S"))
    time.sleep(3)
    print("stop waiting", time.strftime("%H:%M:%S"))
thread1 = threading.Thread(target = doWaiting)
thread1.start()
time.sleep(1)	# 确保thread1已经启动
print("start join")
thread1.join()	# 将一直阻塞，直到thread1运行结束
print("end join")
```





#### 8. 迭代器(Iterator)，生成器(Generator)，可迭代对象(Iterables) 

```
完全理解Python迭代对象、迭代器、生成器 - FooFish-Python之禅
https://foofish.net/iterators-vs-generators.html
```



#### 9. yield和return区别

```
yield是记录上一次运行的位置，下次执行函数通过上一次的状态得到下一次的值
而return直接结束程序，下次执行函数重新执行
```



#### 10. range和xrange区别

```
range直接返回一个列表
xrange返回一个xrange对象，类似于生成器，每次返回一个值，性能较好
如果数据量较小，两者并无明显差别
```



#### 11. 值传递、引用传递

```python
常见于笔试题， 可变对象与不可变对象的效果不同

def test(a):
    a += 1
    
b = 2
test(b)
# 此时b仍然为2， b为不可变对象，不会改变原始值

def test2(a):
    a.append(1)
    
c = [0]
test2(c)
# 此时c为 [0, 1]
```



#### 12. 小整数内存复用

```
（-5:256]
```



#### 13. Python中如何实现匿名函数？ 什么是lambda表达式？

```
常见搭配于map、filter
简单的使用某个功能但不想单独创建一个函数的时候可以使用lambda匿名函数
```



#### 14. Python中有三目运算符吗？

```
C 语言中    表达式 ？ 表达式真 ： 表达式假
Python中    表达式真 if 表达式 else 表达式假
```



#### 15. 如何将一个列表逆序？

```python
a = [1, 2, 3]
a[::-1]
# >>> [3, 2, 1]
# a >>> [1, 2, 3]
a.reverse()
# >>> [3, 2, 1]
# a >>> [3, 2, 1]
```



#### 16. 如何删除列表中的重复元素? 

```
一定不要使用遍历list过程中remove
定义新的list逐个append
使用set排重
```



#### 17. Python正则表达式相关

```
RE库
match与search的区别：  match从头开始搜索， search从任意位置搜索
group分组，findall

正则表达式30分钟入门教程
https://deerchao.net/tutorials/regex/regex.htm
```



#### 18. 平时写单元测试吗？ Python单元测试如何写？ Django呢？

```
Python使用自带unittest库，可以用nosetest跑
Django中使用django.test模块，是对unittest的封装，常用于对数据库的测试
断言assert模式
```



#### 19. Python常用的单元测试库？

```python
mock \ httpretty \ fakeredis \ mixer \ coverage
# mock        生成虚假返回数据，例如调用send_sms方法，使用mock，则系统认为假设返回为真
# httpretty   生成假的返回值，直接截获系统的HTTP请求，并返回预设值
# fakeredis   构造假redis
# mixer       构造随机假数据
# coverage    代码覆盖率
```



#### 20. 谈谈你对Python装饰器的理解并实现简单装饰

```python
装饰器本质就是一个函数，是一个设计模式
从函数定义入口，传入一个函数，并且返回一个函数
是一种python "语法糖"

# 实现一个能够方便打印函数的运行时间的装饰器，装饰器要有参数控制输出时间单位是s还是ms
def timer(time_type='s'):
    def outer(func):
        from functools import wraps
        @wraps(func)
        def decor(*args):
            import time
            start_time = time.time()
            func(*args)
            end_time = time.time()
            d_time = end_time - start_time
            if time_type == 's':
                print("run the func use : %s sec" % round(d_time, 2))
            if time_type == 'ms':
                print("run the func use : %s ms" % int(d_time*1000))
        return decor
    return outer
```



#### 21. Staticmethod、 Classmethod、 Instance method三者的区别和联系？

```python
Staticmethod		# 不传值， 就是与类一起使用的， 明确代码使用位置
Classmethod  		# 传cls
Instance method		# 传self
```



#### 22. 什么是协程？ 跟进程和线程有什么区别？

```
进程和线程都面临着内核态和用户态的切换，耗费大量时间
系统控制的内容在内核态，用户代码的执行在用户态
协程都在用户态执行，由用户控制，不需要操作系统参与，避免了用户态和内核态的切换
Python协程通过yield关键字实现
```



#### 23. 发散性问题，考察软技能

```
1. 知道PEP8吗？ 简单说几条PEP8的规范
2. 用过哪些Python库？
	自带库：datetime，re，threading， multiprocessing …
	第三方库：requests，MySQL-python，redis，Django，celery …
	单元测试的库
```



#### 24. 数据库事务的特性，什么场景下要使用事务？

```
原子性(Atomicity) - 事务中的所有操作要么全部执行，要么都不执行
一致性(Consistency) - 事务执行之前和执行之后都必须处于一致性状态
隔离性(Isolation) - 多个并发事务之间要相互隔离（后面专门会讲）
持久性(Durability) - 事务一旦被提交了，那么对数据库中的数据的改变就是永久性的

使用场景：1）原子性操作；
		2）并发访问控制（和锁配合）
```



#### 25. MySQL事务和锁的关系 

```
二者不是一个维度的概念：事务是原子操作和访问隔离，锁是数据访问控制
二者经常一起出现：锁（select_for_update）要在事务中才能生效
事务中不一定要有锁
```



#### 26. MySQL InnoDB引擎的事务隔离级别

```
Innodb四个事务隔离级别，MySQL默认使用RR级别
脏读 – 读到了数据库中未提交的数据
不可重复读 – 一个事务内多次查询结果不一致
幻读 – 读到了之前不存在的新纪录（insert）
```

![](https://github.com/JiaxingZhao/Python--Antic/blob/master/img/1534302969970.png)



#### 27. Innodb索引、联合索引，卡丁值(Cardinality) 

```
索引的意义在于提高查询效率，会大幅影响写入速度
Innodb索引存储结构：B+树。由计算机的内存-机械硬盘两层存储结构决定
可以使用索引的情况：
	where 条件中
	order by
	group by
卡丁值太低不要加索引，区分度太低。比如性别、状态
联合索引符合最左前缀原则
```

![](https://github.com/JiaxingZhao/Python--Antic/blob/master/img/1534303067466.png)



#### 28. Redis支持事务吗？ 

```
支持，但是和数据库的事务概念不完全一致
坑！非原子性,不支持回滚：Redis在事务失败时不进行回滚，而是继续执行余下的命令
不回滚的原因：1.只有语法错误会失败，开发阶段就应该发现
             2.不回滚保持Redis简单
MULTI 、 EXEC 、 DISCARD 和 WATCH 是 Redis 事务的基础
也可以用Pipeline实现批量提交命令（非事务）
```



#### 29. Redis高可用方案？

```
master-slave
sentinel自动flavor
集群：Redis Cluster（官方）、Codis （豌豆荚）
```



#### 30. 数组、链表、Hash表/字典区别，并举例说明各自的应用场景

```
数组 – 连续空间; 随机访问O(1); 插入、删除元素O(n)。储存一个月每天的温度
链表 - 非连续空间；随机访问O(n)；插入、删除元素O(1)。储存行程计划
Hash表/字典 - 非连续空间；随机访问O(n)；插入、删除O(1)；不重复。储存班级每人成绩
```



#### 31. 栈、队列的区别，举例各自的应用场景 

```
栈 – 先进先出；支持push、pop、top操作。函数的调用关系
队列 – 先进先出。按顺序执行的消息队列
双端队列 – 两端都可以进出。既可当栈使用，也可当队列使用
```



#### 32. 常见排序算法实现，稳定性，及其时间复杂度、空间复杂度 

![](https://github.com/JiaxingZhao/Python--Antic/blob/master/img/1534314173618.png)



#### 33.  谈谈你对几种不同Python web框架的认识和理解

```
Django、Tornado、Flask、Bottle
```



#### 34. Django中间件相关 

```
什么是Django中间件？
什么场景下使用Django中间件？
实现一个中间件主要实现的两个方法：process_request和process_response
Django中间件请求阶段和响应阶段的执行顺序？
```

![](https://github.com/JiaxingZhao/Python--Antic/blob/master/img/1534314262045.png)



#### 35. Django的session模块

```
Django session通过客户端cookie存放sessionid + 服务端序列化存储实现
使用： django.contrib.sessions  INSTALLED_APPS   + SessionMiddleware   MIDDLEWARE
Django session支持多种存储引擎：db，cache，cached_db，file，cookie
Django session 有domain限制。.example.com  sub.example.com
可以在request.session直接读取
```



#### 36. Django的Auth模块

```
User、Permissions、Groups、password、login
使用：django.contrib.auth   INSTALLED_APPS  + AuthenticationMiddleware   MIDDLEWARE
依赖session模块
最佳实践：基于AbstractUser实现自己的User类
如何安全的存储密码？           Hash + Salt
```



#### 37. 谈一下Django中的安全机制 

```
XSS (跨域脚本攻击)   - 模板转义 （ 直接写script脚本 ）
CSRF（跨站提交请求） -  CsrfViewMiddleware
常量密码验证时间
```



#### 38. Django的缓存机制

```
为什么要使用cache？
cache抽象成基本操作：get、set、delete、expire
backend：支持memcached、db、file、local-memory
使用：1）通过settings.py中的CACHE配置；
	 2）from django.core.cache import cache
```



#### 39. Django如何实现RESTful接口 

```
class-based view
理解RESTful架构 - 阮一峰的网络日志
http://www.ruanyifeng.com/blog/2011/09/restful.html
RESTful API 设计指南 - 阮一峰的网络日志
http://www.ruanyifeng.com/blog/2014/05/restful_api.html
```

![](https://github.com/JiaxingZhao/Python--Antic/blob/master/img/1534314401023.png)

![](https://github.com/JiaxingZhao/Python--Antic/blob/master/img/1534314404356.png)



#### 40.  简述HTTP协议的特点，列举几个常见的HTTP HEAD 

```
HTTP（超文本传输协议）是一个基于请求与响应模式的、无状态的、应用层协议，基于TCP连接
Context-type
Cookie
Accept-Language
Referer
Cache-Control
If-Modified-Since、Last-Modified

五层： 应用层、网络层、传输层、数据链路层、物理层
```



#### 41.HTTP请求报文的三部分，HTTP响应报文的三部分 

```
请求报文三部分：请求行、消息报头、请求正文
响应报文三部分：状态行、消息报头、响应正文
```

![](http://dl.iteye.com/upload/attachment/0069/3451/412b4451-2738-3ebc-b1f6-a0cc13b9697b.jpg)

![](http://dl.iteye.com/upload/attachment/0069/3492/bddb00b6-a3e1-3112-a4f4-4b3cb8687c70.jpg)



#### 42. HTTP错误码的划分,说出几个常见的错误码  

| 状态码         | 定义                                            |
| -------------- | ----------------------------------------------- |
| 1xx 报告       | 接收到请求，继续进程                            |
| 2xx 成功       | 步骤成功接收，被理解，并被接受 (200)            |
| 3xx 重定向     | 为了完成请求,必须采取进一步措施 (301、302、304) |
| 4xx 客户端出错 | 请求包括错的顺序或不能完成 (400、403、404、405) |
| 5xx 服务器出错 | 服务器无法完成显然有效的请求（500、502、504）   |