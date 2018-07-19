#coding:utf-8


'''
Created on 2018年3月21日

@author: caideyang


使用递归函数实现快速排序算法
'''
def quickSort(List):
    if len(List) < 2:
        return List
    else:
        privot = List[0]
        small = [ number for number in List[1:] if number <= privot ]
        big = [ number for number in List[1:] if number > privot ]
        return quickSort(small) + [privot] + quickSort(big)
    
if __name__ == "__main__":
    print(quickSort([34,14,37,23,128,56,79,12]))