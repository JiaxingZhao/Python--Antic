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

为了施加一种自然地顺序，必须要有某种规则来比较各项，例如：$$item_i <= item_{i+1}$$   以便能够访问有序集合中的各个项。

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

​	前面的两个循环，第一个循环在问题数量为n时执行了n次，第二个循环在问题数量为n时执行了n*n次

​	第一个算法的性能时线性的，第二个算法的行为是二次方阶的。如果一个算法对于任何的问题规模，都需要相同的操作次数，那么他拥有常数阶的性能，列表索引就是常数时间算法的一个例子，是性能最好的一类算法。

​	对数阶比线性阶好一点，但比常数阶差一点，对数阶的工作量和问题规模的log2成比例。当问题规模翻倍的时候，其工作量只增加1。

|    n    | 对数阶($$log_2n$$) | 线性阶($$n$$) |  平方阶($n^2$)   | 指数阶($$2^n$$) |
| :-----: | :-------------: | :--------: | :-----------: | :----------: |
|   100   |        7        |    100     |     10000     |      超标      |
|  1000   |       10        |    1000    |    1000000    |      超标      |
| 1000000 |       20        |  1000000   | 1000000000000 |     严重超标     |



#### 3.3 搜索算法

##### 3.3.1 搜索最小值

```python
'''
这个算法必须访问列表中的每一项以确保找到了最小项的位置，因此，对于大小为n的列表，该算法必须进行n-1次比较，因此，算法的复杂度为O(n)
'''

def ourMin(lyst, trace = False):
    """Returns the position of the minimum item."""
    minpos = 0
    current = 1
    while current < len(lyst):
        if lyst[current] < lyst[minpos]:
            minpos = current
            if trace: print current, minpos
        current += 1
    return minpos
```



##### 3.3.2 顺序搜索一个列表

```python
'''
从第一个位置的项开始，将其与目标项进行比较，如果两个项相等，返回true，否则移动到下一个位置进行比较，如果到了最后一个位置，返回false，这种搜索叫作顺序搜索（sequential search）或线性搜索（linear search）
'''
def linearSearch(target, lyst, profiler):
    """Returns the position of the target item if found,
    or -1 otherwise."""
    position = 0
    while position < len(lyst):
        profiler.comparison()
        if target == lyst[position]:
            return position
        position += 1
    return -1
```



##### 3.3.3 最好情况、最坏情况和平均情况的性能

顺序搜索要考虑三种情况：

​	1、最坏情况下，目标向位于末尾，或者就不在列表中。那么算法必须访问每一个项，并且对大小为n的列表执行n次迭代，因此，顺序搜索最坏情况的复杂度为O(n)

​	2、最好情况下，第一次迭代就找到了对象，这种情况的复杂度为O(1)

​	3、平均情况下，把每一个可能的位置找到目标向所需的迭代次数相加，并且用总和除以n，因此算法执行了（n+n-1+n-2+···+1)/n 或者 (n+1)/2次的迭代，对于很大的n，常数因子2的作用并不大，因此复杂度为O(n)



##### 3.3.4 有序列表的二叉搜索

​	当搜索没有特定顺序排列的数据，顺序搜索是必要的，当搜索排序的数据时，可以用二叉搜索

​	假设列表中的项都是升序的，那么直接与中间位置对比，相等返回，小于搜前段，大于搜后段，二叉搜索的最坏情况的复杂度为 $$O(log_2n)$$

```python
def binarySearch(target, lyst, profiler):
    """Returns the position of the target item if found,
    or -1 otherwise."""
    left = 0
    right = len(lyst) - 1
    while left <= right:
        profiler.comparison()
        midpoint = (left + right) // 2
        if target == lyst[midpoint]:
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1
```



##### 3.3.5 比较数据项

​	二叉搜索和搜索最小项，都是假设列表中的项是可以互相比较的，使用 __ eq __ , __ lt __ , __ gt __方法来实现

```python
class SavingsAccount(object):
    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance
        
        def __lt__(self, other):
            return self._name < other._name
```



##### 3.3.6 练习3.3

​	1、假设一个列表在索引0到9的位置上，包含了值20、44、48、55、62、66、74、88、93和99，用二叉搜索法搜索目标值90.记录搜索中左边右边和中间点的值，对于目标值44重复这个过程。

Solution :

```python
def search(target, slist):
    left = 0
    right = len(slist) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == slist[mid]:
            return mid
        elif target < slist[mid]:
            right = mid - 1
        elif target > slist[mid]:
            left = mid + 1
    return -1
```



#### 3.4 基本排序算法

##### 3.4.1选择排序

​	最简单的策略就是搜索整个列表，对比两项是否满足条件，满足则交换位置

```python
def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = I
        j = i + 1
        while j < len(lyst):
            if lyst[i] < lyst[minIndex]:
                minIndex = j
                j += 1
        if minIndex != 1:
            swap(lyst, minIndex, I)
        i += 1
```

​	该函数包含了一个嵌套循环，对于大小为n的列表，外围循环执行n-1次，第一次通过外围循环的时候，内部循环n-1次，第二次通过外围循环时，循环n-2次： 这种情况的复杂度为 $$O(n^2)$$

​	$$(n-1)+(n-2)+···+1 = n(n-1) / 2 = \frac{1}{2}n^2-\frac{1}{2}n$$

#### 	