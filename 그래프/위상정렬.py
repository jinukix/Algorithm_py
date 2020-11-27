"""
위상 정렬은 정렬 알고리즘의 일종이다.

방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것이다.

1. 진압차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌때 까지 다음 과정을 반복한다.
- 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
- 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

위상 정렬은 사이클이 존재하지 않는 방향 그래프에서만 적용이 된다.
만약 모든 원소를 방문하지 않았는데 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.

"""

import sys
from collections import deque


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
