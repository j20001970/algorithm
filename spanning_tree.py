#!/usr/bin/python
import sys
from pprint import pprint
# 我的邊
edges = [
    ['A', 'B', 12],
    ['A', 'C', 8],
    ['A', 'D', 13],
    ['B', 'C', 21],
    ['B', 'E', 32],
    ['B', 'F', 7],
    ['C', 'F', 2],
    ['D', 'G', 9],
]

# graph = {
#     'A':{'B':12, 'C':8, 'D':13},
#     'B':{'A':12, 'C':21, 'E':32, 'F':7},
#     'C':{'A':8, 'B':21, 'F':2},
#     'D':{'A':13, 'G':9},
#     'E':{'B':32},
#     'F':{'B':7, 'C':2},
#     'G':{'D':9}
# }

# 造訪節點,能從src走到dest時回傳True,否則False
def traverse_node(src, dest, graph, visited = []):
    m_visited = visited if visited else []
    if not src in m_visited and src in graph:
        m_visited.append(src)
        if dest in graph[src]:
            return True
        for neighbor in graph[src]:
            if traverse_node(neighbor, dest, graph, m_visited):
                return True
    else:
        return False

# 檢查新加入的邊是否與目前的邊形成cycle,無cycle回傳True,cycle回傳False
def check_loop(new_edge, current_edges):
    # 把邊打成圖,無權重
    m_graph = {}
    for e in current_edges:
        if not e[0] in m_graph:
            m_graph[e[0]] = []
        m_graph[e[0]].append(e[1])
        if not e[1] in m_graph:
            m_graph[e[1]] = []
        m_graph[e[1]].append(e[0])
    return not traverse_node(new_edge[0], new_edge[1], m_graph)

# kruskal 演算法
def kruskal(edges):
    # 紀錄選取的邊
    selected = []
    # 依權重排序邊
    edges = list(sorted(edges, key=lambda item: item[2]))
    for e in edges:
        # 如果沒有構成cycle就把邊推進selected
        if(check_loop(e, selected)):
            selected.append(e)
    print(selected)


        

# kruskal(edges)
# prim(edges, 'A')