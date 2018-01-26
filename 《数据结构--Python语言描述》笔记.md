# 《数据结构 （Python语言描述）》 -- 笔记



### 第二章 -- 集合概览

集合（collection） 是可以作为概念性的单位来处理的一组零个或多个项。



#### 2.1 集合类型

包括：字符串、列表、元组、集、字典 ； 栈、队列、优先队列、二叉树、堆、图、包

集合可以是同构的也可以是异构的，通常是动态而不是静态的，内容是可以改变的，但不可变类型除外



##### 2.1.1 线性集合

​	线性集合按照位置来有序的，除了第一项以外，都有唯一前驱，除了最后一项，都有唯一后继



##### 2.1.2 层级集合

​	其中的数据项在结构中的顺序类似于一棵上下颠倒的树，除了最顶端的第一个数据项，每个数据项都只有一个前驱，但可能有多个后继，文件目录、组织结构树、都是层级集合

##### 2.1.3 图集合

​	图集合也叫作图，每一项都可能有多个前驱或者后继，每一项之间也称作为邻居

##### 2.1.4 无序集合

​	无序集合中的项没有特定的顺序，也没有前驱和后继

##### 2.1.5 有序集合

​	有序集合在其项之上施加了一个自然地顺序，类似电话簿中的条目和班级花名册的条目

为了施加一种自然地顺序，必须要有某种规则来比较各项，例如：
$$
item_i <= item_{i+1}
$$
以便能够访问有序集合中的各个项。

有序集合并不需要是线性的或者是按照位置来排序的，集、包、字典都有可能是有序的，即便他们并不是按照位置来访问的，二叉搜索树也是在各项上施加了一种自然的顺序。

​

##### 2.1.6 集合类型的分类

- ##### 集合

  - ##### 图集合

  - ##### 层级集合

    - ##### 二叉搜索树

    - ##### 堆

  - 线性集合

    - 列表
      - 有序列表
    - 队列
      - 优先队列
    - 栈
    - 字符串

  - 无序集合

    - 包
      - 有序包
    - 字典
      - 有序字典
    - 集
      - 有序


#### 2.2 集合上的操作

操作： len 、in 、 for 、str 、== 、+ 、转换、插入、删除、替换、访问或获取



#### 2.4 小结

- 集合是保存0个或多个其他对象的对象，集合拥有访问对象、插入对象、删除对象、确定集合的大小以及遍历或访问集合的对象的操作
- 集合的5个主要类别是：线性集合、层次集合、图集合、无序集合、有序集合
- 线性集合按照位置来排列其项，除了第一项，每一项都有唯一的一个前驱，除了最后一项，每一个项都有唯一的一个后继
- 层次集合中的项都拥有唯一的前驱（只有一个例外，就是顶层的项），以及0个或多个后继，单个的称为跟的项是没有前驱的。
- 图集合中的项拥有0个或多个前驱，以及0个或多个后继
- 无序集合中的项没有特定的顺序
- 集合是可迭代的，可以用一个for循环来访问包含在集合中的每一项
- 抽象的数据类型是一组对象，以及这些对象上的操作。因此，集合是抽象数据类型。
- 数据结构是表示集合中包含的数据的一个对象。




### 第三章 -- 搜索、排序和复杂度分析

​	算法是计算机程序的一个基本的构建模块。算法描述了最终能够解决一个问题的计算过程。最基本的标准是争取性，可读性和易维护性也是重要的质量指标，还有运行时间性能。

运行一个算法的时候，会消耗两种资源：处理时间和空间或内存。

复杂性分析工具可以评估算法的运行时间性能或效率。



#### 3.1 评估算法的性能

​	当选择算法的时候，必须解决时间、空间平衡问题。



##### 3.1.1 度量算法的运行时间

​	使用计算机的时钟来获取一个实际得运行时间。这个过程叫作基准评价（benchmarking）或探查（profiling）。方法是先计算出几个具有相同大小的不同数据集合的时间，然后计算出平均时间。针对越来越大的数据集合收集相似的数据，在几次测试之后，有了足够的数据能够预测算法对于任何大小的一个数据集合的表现了。

```python
"""
File: timing1.py
Prints the running times for problem sizes that double,
using a single loop.
"""

import time

problemSize = 10000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    
    start = time.time()
    # The start of the algorithm
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    # The end of the algorithm
    elapsed = time.time() - start
    
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
```

```python
"""
File: timing2.py
Prints the running times for problem sizes that double,
using a nested loop.
"""

import time

problemSize = 1000
print("%12s%10s" % ("Problem Size", "Seconds"))
for count in range(5):
    
    start = time.time()
    # The start of the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1
   # The end of the algorithm
    elapsed = time.time() - start
    
    print("%12d%10.3f" % (problemSize, elapsed))
    problemSize *= 2
```

​	1、不同硬件平台的处理速度不同，在不同操作系统上也是不同的。

​	2、对于很大的数据集合来说，确定某些算法的运行时间是不切实际的。



##### 3.1.2 统计指令

​	用于估算算法性能的另一种技术，是统计对不同的问题规模所要执行的指令的数目。不管算法在什么平台上运行，这个统计数字对预算法要执行的抽象的工作量给出了一个很好的预计。

​	当使用这种方式分析算法的时候，需要区分两类指令：

​	1、不管问题规模多大，都执行相同次数的指令

​	2、根据问题的规模，执行不同次数的指令



##### 3.1.4 练习3.1

​	1、编写一个测试程序，统计并显示如下循环的迭代次数

```python
while problemSize > 0:
    problemSize = problemSize // 2
```

solution :

```python
problemSize = 1000
print("%12s%15s" % ("Problem Size", "Iterations"))
number = 0
while problemSize > 0:
    problemSize = problemSize // 2
    number += 1
    
print("%12d%15d" % (problemSize, number))
```

​	2、分别使用1000、2000、4000、10000和100000运行，随着问题规模扩大10倍，迭代次数有什么变化？

solution :

```python
# 分别为10次、11次、12次、14次、17次；问题规模每扩大10倍，迭代次数增加3次
```

​	3、两次调用time.time()的差，就是经过的时间，由于操作系统可能只是在这段时间的一部分之中会使用CPU，经过的时间可能并不能反映出python代码段使用cpu的实际时间，浏览python文档，找到一种替代的方法来记录处理时间，并说明这种方法应该如何做。

solution :

```python
'''
计算程序运行时间一共有三种方法，  datetime.datetime.now()  /  time.time()  /  time.clock()
方法二和方法三返回的位浮点数
其中前两种计算包含其它程序使用CPU的时间， 只有第三种time.clock()只有当前程序运行的时间
在 Unix 系统中，建议使用 time.time()，在 Windows 系统中，建议使用 time.clock()
import time
start = time.clock()
function()
end = time.clock()
print (str(end - start))
'''
```



#### 3.2 复杂度分析

##### 3.2.1 复杂度的阶

​	