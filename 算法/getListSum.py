#encoding:utf-8
"""
使用递归函数来求取列表里的数字总和


"""

def Sum(List):
    # global result
    # if len(List) > 1:
    #     result = List[0] + Sum(List[1:])
    # else:
    #     result = List[0]
    # return result
    return 0 if  List == [] else List[0] + Sum(List[1:])

if __name__=="__main__":
    print(Sum([1,2,3,4,5,6,7,8,9,10]))