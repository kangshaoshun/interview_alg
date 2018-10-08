#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
拓扑排序
"""

class Solution(object):
    def indegree0(self, v, e):
        if not v:
            return
        tmp = v[:]
        for item in e:
            if item[1] in tmp:
                tmp.remove(item[1])
        #有循环
        if not tmp:
            return -1
        #删除以入度为0的节点开始的边
        for t in tmp:
            for ind in range(len(e)):
                if t in e[ind]:
                    e[ind] = 'del'
        if e:
            eset = set(e)
            eset.remove('del')
            e[:] = list(eset)
        #从v中删除tmp中的节点，因为遍历过了
        if v:
            for t in tmp:
                v.remove(t)
        return tmp


    def topoSort(self, v, e):
        result = []
        while True:
            nodes = self.indegree0(v, e)
            if nodes == -1:
                print "has cycle"
                break
            if nodes == None:
                break
            result.extend(nodes)
        return result


if __name__ == '__main__':
    so = Solution()
    #v = ['a','b','c','d','e']
    #e = [('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]
    v = [0, 1]
    e = [[0, 1]]
    print so.topoSort(v, e)
