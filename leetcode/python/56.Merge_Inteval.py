#coding:utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x:x.start)
        res_list = []
        tmp = None
        for item in intervals:
            if tmp:
                if tmp.end < item.start:
                    res_list.append(tmp)
                    tmp = item
                else:
                    tmp.end = max(tmp.end, item.end)
            else:
                tmp = Interval(item.start, item.end)
        res_list.append(tmp)       
        return res_list
