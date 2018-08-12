#### 1. 简单谈一下你对Python这门语言的理解

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



#### 6. Python多进程编程

```
multiprocessing模块
基础方法跟threading类似
锁也跟threading类似
神器multiprocessing.dummy
```



#### 7. Pyhton多进程编程如何共享数据

```
multiprocessing.Value 和 multiprocessing.Array
Queue
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
# mock 生成虚假返回数据，例如调用send_sms方法，使用mock，则系统认为假设返回为真
# fakeredis  构造假redis
# mixer  构造随机假数据
# coverage  代码覆盖率
```



#### 20. 谈谈你对Python装饰器的理解并实现简单装饰

```python
装饰器本质就是一个函数，是一个设计模式
从函数定义入口，传入一个函数，并且返回一个函数
是一种python "语法糖"

# 实现一个能够方便打印函数的运行时间的装饰器，装饰器要有参数控制输出时间单位是s还是ms
def timer(time_type='s'):
    def outer(func):
        def decor(*args):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            if time_type == 's':
                d_time = int(end_time - start_time)
                print("run the func use : %s sec" % d_time)
            if time_type == 'ms':
                d_time = end_time - start_time
                d_time = int(d_time * 1000)
                print("run the func use : %s ms" % d_time)
        return decor
    return outer
```



#### 21. Staticmethod、 Classmethod、 Instance method三者的区别和联系？

```python
Static method		# 不传值， 就是与类一起使用的， 明确代码使用位置
Class method		# 传cls
Instance method		# 传self
```



#### 22. 什么是协程？ 跟进程和线程有什么区别？

```
进程和线程都面临着内核态和用户态的切换，耗费大量时间
系统控制的内容在内核态，用户代码的执行在用户态
协程都在用户态执行，由用户控制，不需要操作系统参与，避免了用户态和内核态的切换
Python协程通过yield关键字实现
```