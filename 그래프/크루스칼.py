"""
크루스칼 알고리즘은 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘이다.
즉 최소 신장 트리를 찾는 알고리즘이라고도 할 수가 있다.

신장트리 : 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프.

크루스칼 알고리즘의 동작은 간단하다.

1. 간선 데이터를 비용에 따라 오름차순으로 정렬.
2. 간선을 하나씩 확인 해 현재 간선이 사이클을 발생시키는지 확인해 사이클이 발생하지 않는다면 신장 트리에 포함.

"""

import sys


def read():
    return sys.stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수, 간선의 개수
v, e = map(int, read().split())
parent = [0 for i in range(v+1)]

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b, c = map(int, read().split())
    edges.append([c, a, b])  # a->b 비용 :c

edges.sort()

for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c

print(result)


"""
입력
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

출력
159
"""
