#encoding:utf-8
def mutply(x):
    return x * x

L = map(mutply,[1,2,3,4,5,6,7,8,9])
# print(list(L))


from functools import reduce
def total(x,y):
    return  int(x) + int(y)

print(reduce(total,[1,2,3,4,5,6]))

from functools import reduce
def getNum(x,y):
    return str(x) +str(y)

print(reduce(getNum,[1,2,3,4,56]))


def getStr(x):
    return str(x)

print(list(map(getStr,[1,2,3,4,5])))

def normalize(name):
    return str(name).capitalize()

print(list(map(normalize,['caideyang','CAIDeyang','caiDeyang'])))

