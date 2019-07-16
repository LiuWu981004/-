# List 中各方法的运行时间
time(list(range)) < time([i for i in range]) < time(append) < time(+)

## 底层原理
各功能底层原理，导致的速度差别pass （先挖一个坑以后再来填）


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

