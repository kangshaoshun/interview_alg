#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
最短路径问题
"""


"""
map = [[float('inf')] * 6 for _ in range(6)]

map[0][1], map[0][5] = 6, 1
map[1][2] = 7
map[2][3] = 2
map[4][0], map[4][3] = 2, 3
map[5][2], map[5][4] = 4, 4

tmp = [line for line in map]

#佛洛依德算法
#T = O(N^3)
#它会把所有点之间的最短距离都算出来，这是不足的地方
for i in range(len(tmp)):
    for j in range(len(tmp[i])):
        if j == i:
            continue
        for k in range(len(tmp[i])):
            if k == i or k == j:
                continue
            if tmp[i][j] > tmp[i][k] + tmp[k][j]:
                tmp[i][j] = (tmp[i][k] + tmp[k][j])
"""


#Dijkstra算法
#它的思路是每次取一个松弛变量,如果松弛变量到某一个顶点的值小于原始距离则更新该距离

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}
}

current = 'B'
unvisited = {node:None for node in nodes}
visited = {}
currentDis = 0
unvisited[current] = currentDis

while True:
    for neighbor, distance in distances[current].items():
        if neighbor not in unvisited:continue
        newdis = currentDis + distance 
        if unvisited[neighbor] == None or newdis < unvisited[neighbor]:
            unvisited[neighbor] = newdis
    visited[current] = currentDis
    del unvisited[current]
    if not unvisited:break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDis = sorted(candidates, key=lambda x:x[1])[0]

print visited['D']
