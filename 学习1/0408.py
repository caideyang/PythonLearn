#encoding:utf-8

#获取从3开始的奇数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
#定义一个筛选函数：当传入的值x不能被n整除，则返回True，否则返回False
def _not_avible(n):
    return lambda x: x % n > 0
# print(_not_avible(3)(6))  #输出False
# print(_not_avible(3)(7))  #输出True
# print(list(filter(_not_avible(3),[3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]))) #输出 [5, 7, 11, 13, 17, 19, 23, 25, 29, 31]

#获取素数函数
def primes():
    yield 2 #最小的素数
    it = _odd_iter()  # 初始序列[3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37.....]
    while True:
        n = next(it) #获取序列的第一个值
        yield n  #序列里第一个数为素数，将该数字存于yield迭代
        it = filter(_not_avible(n),it)  #构造新的序列 it
L = []
primes = primes()
for prime in primes:
    if prime < 100:
        L.append(prime)
    else:
        break
print("100以内的素数为：",L)