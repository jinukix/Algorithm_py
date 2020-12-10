"""
1. 분리집합

분리 집합이란 중복 포함된 원소가 없는 집합이다.

분리 집합 자료구조 : 분리 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조.

분리 집합 자료구조를 구현할 때는 트리 자료구조를 이용해 집합을 표현하는데,
기존 트리 구조와는 달리 자식 노드가 부모 노드를 가리키는 형태이다.

분리 집합 탐색 연산은 해당 원소 노드가 속해 있는 집합, 즉 루트 노드를 찾는 연산이다.
분리 집합에선 자식이 부모를 가리키므로 가리키는 부모를 따라 이동하다 보면 루트 노드에 도착하게 된다. 
그 루트 노드를 반환하면 해당 원소 노드가 속해 있는 집합을 알 수 있다. 

Union - Find 두 연산을 사용해 분리 집합 자료구조를 다룰수있다.

union (합집합) : 두 집합을 하나로 합친다. (A의 부모를 B의 부모로 설정하는 것.)
find (집합 탐색) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산. (즉 루트 노드를 찾는 연산)

분리집합 알고리즘 예제

"""

from collections import deque
import sys


def read():
    return sys.stdin.readline().strip()


def find_parnet(parent, x):
    if parent[x] != x:
        parent[x] = find_parnet(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parnet(parent, a)
    b = find_parnet(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, read().split())
parent = [0 for i in range(v+1)]

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, read().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합 : ", end=" ")
for i in range(1, v+1):
    print(find_parnet(parent, i), end=" ")

print()

print("부모 테이블 : ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")

"""
입력
6 4
1 4
2 3
2 4
5 6

출력

각 원소가 속한 집합 :  1 1 1 1 5 5 
부모 테이블 :  1 1 2 1 5 5 

"""

"""

크루스칼 알고리즘

크루스칼 알고리즘은 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘이다.
즉 최소 신장 트리를 찾는 알고리즘이라고도 할 수가 있다.

신장트리 : 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프.

크루스칼 알고리즘의 동작은 간단하다.

1. 간선 데이터를 비용에 따라 오름차순으로 정렬.
2. 간선을 하나씩 확인 해 현재 간선이 사이클을 발생시키는지 확인해 사이클이 발생하지 않는다면 신장 트리에 포함.

"""


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


"""

위상정렬

위상 정렬은 정렬 알고리즘의 일종이다.

방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것이다.

1. 진압차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌때 까지 다음 과정을 반복한다.
- 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
- 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

위상 정렬은 사이클이 존재하지 않는 방향 그래프에서만 적용이 된다.
만약 모든 원소를 방문하지 않았는데 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
"""


def read():
    return sys.stdin.readline().strip()


def topology_sort():
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)


v, e = map(int, read().split())
indegree = [0 for i in range(v+1)]  # 진입차수.
graph = [[] for i in range(v+1)]

for i in range(e):
    a, b = map(int, read().split())
    graph[a].append(b)
    indegree[b] += 1

print(graph)

result = []

topology_sort()

for i in result:
    print(i, end=" ")
"""
입력
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

출력
1 2 5 3 6 4 7
"""
