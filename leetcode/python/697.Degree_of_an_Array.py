#!/usr/bin/python
#coding:utf-8


def comp(x, y):
    if x[1] > y[1]:
        return 1
    if x[1] == y[1] and x[0] < y[0]:
        return 1
    elif x[1] == y[1] and x[0] > y[0]:
        return -1
    else:
        return -1
    
def test():
    li = [1]
    d = dict()
    for index, value in enumerate(li):
        if value in d:
            d[value][0].append(index)
            d[value][1] += 1
        else:
            d[value] = [[],[]]
            d[value][0] = [index]
            d[value][1] = 1
    val = d.values()
    print val
    for item in val:
        item[0] = item[0][-1] - item[0][0] + 1
    val.sort(cmp=comp,reverse=True)
    return val[0][0]
if __name__ == '__main__':
    print test()
