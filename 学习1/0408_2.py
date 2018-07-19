#coding:utf-8
# def getSum(*args):
#     def Sum():
#         total = 0
#         for arg in args:
#             total += arg
#         return total
#     return Sum
# gs = getSum(1,2,3,4,5,6)
# print(gs)
# print(gs())
# def count():
#     fs = []
#     for i in range(1,5):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
# f1,f2,f3,f4 = count()
# print(f1(),f2(),f3(),f4())

# def count():
#     fs = []
#     def f(i):
#         def m():
#             return i * i
#         return m
#     for i in range(1,5):
#         fs.append(f(i))
#     return fs

# f1,f2,f3,f4 = count()
# print(f1(),f2(),f3(),f4())

def createCounter():
    L = [0]
    def counter():
        L[0] += 1
        return L[0]
    return counter
count = createCounter()
print(count(),count(),count())
