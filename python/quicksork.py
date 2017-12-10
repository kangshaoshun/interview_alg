#coding:utf-8
"""
    快速排序的思想是：
        基准数，大于基准数，小于基准数的各在一边
        递归排序每一边

    Time Complexity:O(nlgn)
    Space Complexity:O(nlgn)
"""

def QuickSort(myList, start, end):
    if start < end:
        i, j = start, end
        base = myList[i]
        while i < j:
            while i < j and myList[j] >= base:
                j -= 1
            myList[i] = myList[j]
            while i < j and myList[i] <= base:
                i += 1
            myList[j] = myList[i]
        myList[i] = base
        QuickSort(myList, start, i-1)
        QuickSort(myList, j+1, end)
    return myList


if __name__ == '__main__':
    mylist = [1, 3, 4, 8, 2, 1, 0, 9]
    print QuickSort(mylist, 0, len(mylist)-1)




