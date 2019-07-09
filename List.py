#-*—coding:utf-8-*-
#author : 樱花下丶泪如雨

from timeit import Timer

def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li +=[i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

timer1 = Timer('test1()','from __main__ import test1')
print('append:',timer1.timeit(1000))

timer2 = Timer('test2()','from __main__ import test2')
print('+:',timer2.timeit(1000))

timer3 = Timer('test3()','from __main__ import test3')
print('[i for i in range]:',timer3.timeit(1000))

timer4 = Timer('test4()','from __main__ import test4')
print('list(range):',timer4.timeit(1000))
'''不能传一个函数名，传的函数执行的代码字符串，测算时是在另外的位置测试的，不是在当前文件
所以在测算环境中需要有test1（）函数，所以需要导入函数 from __mian__ import test1
timer.timeit(num) num 是执行次数
'''
