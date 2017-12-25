#coding:utf-8
"""
    选择排序
        思想：它的出发点不在排序，在于挑。每次挑选数组的最值与前置元素置换[挑选 与 置换]
        Time Complexity:O(N^2)
        Space Complexity:O(1)
"""

def selectSort(L):
    assert type(L) == type([''])
    length = len(L)
    if length <= 1:
        return L
    def _max(s):
        largest = s
        for i in xrange(s, length):
            if L[i] > L[largest]:
                largest = i
        return largest
    for i in xrange(length):
        largest =  _max(i)
        if i != largest:
            L[i], L[largest] = L[largest], L[i]
    return L


if __name__ == '__main__':
    a = [3, 5, 8, 1, 2, 9, 10, 21, 24]
    print selectSort(a)
        
