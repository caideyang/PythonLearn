# import binascii as ba
# print(ba.a2b_hex('56352E30344552'))
# print(hex(133))
# print(hex(190))


# def getSum(x,y):
#     return lambda z : (x * x + y * y) * z
#
# print(getSum(3,4))
# print(getSum(3,4)(2))

import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(args,**kw):
#         print("call %s():" %func.__name__)
#         return func(*args,**kw)
#     return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        begin_time = time.time()
        def wrapper(*args, **kw):
            return func(*args, **kw)
        end_time = time.time()
        print("%s函数执行用时:%s" %(func.__name__,end_time-begin_time))
        return wrapper
    return decorator



@log("Text ")
def now():
    print("2015-03-25")

now()
print(now.__name__)