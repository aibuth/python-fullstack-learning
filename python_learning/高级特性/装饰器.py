def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print('2026-05-07')
now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2026-05-09')
now()


import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper
@log
def now():
    print('2026-05-09')
now()


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2026-05-09')

now()





#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print('%s executed in %.4f ms' % (fn.__name__, elapsed_time))
        return result
    return wrapper
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x + y
@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x * y * z
f = fast(11,22)
s = slow(11,22,33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')



#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
def log(text = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(text, str):
                print(f'begin call {text}')
            else:
                print('begin call')
            result = func(*args, **kwargs)
            print('end call')
            return result
        return wrapper
    if callable(text):
        func = text
        return decorator(func)
    else:
        return decorator

@log
def f1():
    print('f1正在执行...')

@log('execute')
def f2():
    print('f2正在执行...')
f1()
f2()