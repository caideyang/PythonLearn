#encoding:utf-8
import time,functools
def metric(func):

    @functools.wraps(func)
    def wrapper(*args,**kw):
        begin_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        print("%s函数执行用时:%s" % (func.__name__, end_time - begin_time))
        return result
    return wrapper

@metric
def fast(x, y):
    # time.sleep(2.0012)
    for i in range(y):
        x *= y
    return x

print(fast(2,1213))