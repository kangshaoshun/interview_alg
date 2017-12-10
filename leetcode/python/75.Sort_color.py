#coding:utf-8
"""
    题意：快排
"""

class Solution(object):
    def quickSort(self, mylist, start, end):
        if start < end:
            i, j = start, end
            base = mylist[i]
            while i < j:
                while i < j and mylist[j] >= base:
                    j -= 1
                mylist[i] = mylist[j]
                while i < j and mylist[i] <= base:
                    i += 1
                mylist[j] = mylist[i]
            mylist[i] = base
            self.quickSort(mylist, start, i-1)
            self.quickSort(mylist, j+1, end)
        return mylist

    def sortColors(self, nums):
        return self.quickSort(nums, 0, len(nums)-1)


if __name__ == '__main__':
    mylist = [1, 3, 4, 2, 8, 5, 4]
    s = Solution()
    print s.sortColors(mylist)
