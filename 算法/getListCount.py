#encoding:utf-8

"""
使用递归函数获取列表的元素个数
"""

def getListCount(List):
    return 0 if List == [] else 1+ getListCount(List[1:])

if __name__ == "__main__":
    print(getListCount([1,2,3,4,5,'a']))