#coding:utf-8
"""
    冒泡排序算法
        思想：两层循环，两两向后比较
        Time Complexity:O(N^2)
        Space Complexity:O(1)
"""
def bubbleSort(L):
    assert type(L) == type([''])
    length = len(L)
    if L <= 1:
        return L
    for i in xrange(length):
        for j in xrange(length-i-1):
            if L[j] < L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L



if __name__ == '__main__':
    a = [3, 5, 8, 1, 2, 9, 10, 21, 24]
    print bubbleSort(a)
