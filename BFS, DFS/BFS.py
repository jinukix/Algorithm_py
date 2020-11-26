"""

BFS 너비 우선 탐색.

Breath-First Search.

너비 우선 탐색이라고 불리며, 쉽게 말하자면 가까운 노드부터 탐색하는 알고리즘이다.
DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식인데, BFS는 그 반대이다.
또 BFS 구현에는 DFS와 달리 큐 자료구조를 이용하는 것이 정석이고, 재귀적으로 동작하지 않는다.
인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 설계하면, 자연스럽게 먼저 들어온 것이 
먼저 나가게 되어, 가까운 노드부터 탐색을 진행할수 있기 때문이다.
DFS보다는 조금 더 빠르게 동작한다.

"""

# BFS 예제

from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:  # 큐가 빌 때까지.
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False for i in range(9)]

bfs(graph, 1, visited)
