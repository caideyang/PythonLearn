#encoding:utf-8

"""
使用递归函数获取列表中最大数字
"""
def getMaxNumberInList(List):

    if len(List) < 2 :
        return List[0]
    if List[0] > List[1]:
        List[1] = List[0]
    return getMaxNumberInList(List[1:])

if __name__ == "__main__":
    print(getMaxNumberInList([170,21,213,14,45]))