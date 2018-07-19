#coding:utf-8

def triangles():
    L = [1]
    yield L
    L = [1,1]
    yield L
    L = [1,2,1]
    while True:
        L = [L[i]+L[i+1] for i in range(len(L))]
        L.insert(0,1)
        L.append(1)
        yield L


if __name__ == "__main__":
    n = 5
    while n > 0:
        print(next(triangles()))
        n -= 1

