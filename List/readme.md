# List 中各方法的运行时间
time(list(range)) < time([i for i in range]) < time(append) < time(+)

## 底层原理
### list
list作为一种线性的数据存储结构，在内存中划分连续的存储空间进行数据存储。在数据区头部有信息区存储list的最大容量和当前元素个数的信息。若采用分离式存储，则信息区还有数据区的首地址，用来定位数据区。分离式存储比连续存储有一定的好处，故Python中list的数据存储是采用分离式存储实现的。
### dict
Python中的dict数据类型采用hash存储方式。数据类型分为key和value两部分，先把key转换为int类型再对存储区域长度取余，若产生冲突，则开放寻址直到找到存储位置为止。注意的是dict初始状态为unused时，key，value都是Null，插入元素后就变成了active状态，删除后为dummy状态，可以在再次插入时变为active状态，但是再也变不成unused状态了。dummy状态实际上是一种伪删除的状态，保证探测链的完整性，否则完全删除后，该数据后面的数据就无法被操作了。


# 运算时间
## timeit
官方连接 https://docs.python.org/3/library/timeit.html  
 Timer('执行的字符串','导入位置')  返回执行时间
 实现的原理是：将传入的代码字符串在另外的位置进行速度测试，不是在当前文件的位置。
 所以将需要测试的字符串打包成一个函数整体，把函数名传过去，然后引入函数的路径。

timeit(num) 其中num 是执行次数
## datetime
datetime.datetime.now()返回当前日期。在程序开始和结束时分别获取当前日期，做差转换成秒就可以得到程序的运行时间了。

## time
time.time 获取当前的时间（单位是秒）类似datetime，在程序开始和结束位置打上时间戳做差即可得到运行时间。
time.clock()得到的是CPU的执行时间。 
程序的执行时间 = CPU的执行时间 + IO口传输时间 + 等待时间
所以clock()得到的是真正用于计算的时间。

# 知识
## 一阶知识
测量代码的执行时间，有三种方法timer， time.time， datetime.datetime.now
## 二阶知识
timer与需要测算运算速度的函数之间相互组合

