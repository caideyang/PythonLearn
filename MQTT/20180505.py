#encoding:utf-8
# def getCount():
#     sum = 0
#     for i in range(10000):
#         sum += i
#         yield sum
#


# def customer():
#     while True:
#         name = yield
#         print("%s 准备吃..." % name)
#
# def producer():
#     pass
#
# c1 = customer()
# c1.__next__()
# t1 = c1.send("Caideyang")
# t2 = c1.send("deyang")


# def getLines(file):
#     with open(file,'r',encoding="utf-8") as f:
#         for line in f:
#             print(line)
#             yield line
#
# file = getLines('log.txt')
# file.__next__()
# file.__next__()
# file.__next__()
# file.__next__()
# file.__next__()

def fun(name,*args,**kwargs):
    print(name,args,kwargs)
    if "age" in kwargs.keys():
        print(kwargs['age'])

fun('caideyang')
fun('caideyang',12)
fun('caideyang',12,13,age=15,salary=19000)


