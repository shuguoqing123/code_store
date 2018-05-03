#encoding:utf-8

'''

根据工程规则，已经成型的代码最好不要修改，如果要添加功能，应该最好再次进行封装。
装饰器可以达到这样的目的。
'''

# 1、比如有四个方法暴露给客户使用,一般情况如下：


def f1():
    print 'f1'


def f2():
    print 'f2'


def f3():
    print 'f3'


def f4():
    print 'f4'


f1()
f2()
f3()
f4()


# 2、如果要求在调用方法之前需验证操作，可以使用装饰器，在方法之上再封装验证功能：
#针对不同参数列表的函数也可以进行统一的装饰。

def w(func):
    def inner(*args, **kwargs):
        print '验证操作'
        return func(*args, **kwargs)
    return inner


@w
def f1(arg):
    print 'w-f1'+str(arg)


@w
def f2(arg1, arg2):
    print 'w-f2'+str(arg1)+str(arg2)


@w
def f3(arg1, arg2, arg3):
    print 'w-f3'+str(arg1)+str(arg2)+str(arg3)


@w
def f4():
    print 'w-f4'


f1(1)
f2(1, 2)
f3(1, 2, 3)
f4()


# 3、一个函数也可以被不同的装饰器封装

def w1(func):
    def inner(*args, **kwargs):
        print '验证操作1'
        return func(*args, **kwargs)
    return inner


def w2(func):
    def inner(*args, **kwargs):
        print '验证操作2'
        return func(*args, **kwargs)
    return inner


@w1
@w2
def f1(arg):
    print 'w-f1'+str(arg)


@w1
@w2
def f2(arg1, arg2):
    print 'w-f2'+str(arg1)+str(arg2)


@w1
@w2
def f3(arg1, arg2, arg3):
    print 'w-f3'+str(arg1)+str(arg2)+str(arg3)


@w1
@w2
def f4():
    print 'w-f4'


f1(1)
f2(1, 2)
f3(1, 2, 3)
f4()


def before(request, kargs):
    print 'before'
    return 'before'


def after(request, kargs):
    print 'after'
    return 'after'


def filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):

            before_result = before_func(request, kargs)
            if before_result!=None:return before_result

            main_result = main_func(request, kargs)
            if main_result != None:return main_result

            after_result = after_func(request, kargs)
            if after_result != None:return after_result

        return wrapper
    return outer


@filter(before, after)
def index(request, kargs):
    print 'index'

index(1,2)
