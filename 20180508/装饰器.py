#encoding:utf-8
import time

def timer(func):
    def warpper(*args,**kwargs):
        begin_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print("函数执行用时%s" %(end_time - begin_time))
        return res
    return warpper

# @timer 相当于func = timer(func)
@timer
def func(name):
    print("正在执行 %s" % name)
    time.sleep(2)
    return "Hello"


print(func("caideyang"))
# func = timer(func)
# func("Caideyang")