"""

DFS 깊이 우선 탐색.

Depth-First Search.

깊이 우선 탐색이라고도 불리며, 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
루트 노드로 시작해 다음 분기로 넘어가기 전에 해당 분기를 최대한 '깊숙이' 탐색하는 방법이다.
BFS와 달리 스택 자료구조를 이용하는 것이 정석이며, 재귀함수로도 구현을 하기도 한다.
BFS보다는 조금 느리게 동작한다.

"""

# DFS 예제


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


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

dfs(graph, 1, visited)
