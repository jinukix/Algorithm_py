"""

탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.
대표적인 탐색 알고리즘으로는 DFS와 BFS를 꼽을 수 있다

1. DFS 깊이 우선 탐색.

Depth-First Search.

깊이 우선 탐색이라고도 불리며, 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
루트 노드로 시작해 다음 분기로 넘어가기 전에 해당 분기를 최대한 '깊숙이' 탐색하는 방법이다.
BFS와 달리 스택 자료구조를 이용하는 것이 정석이며, 재귀함수로도 구현을 하기도 한다.
BFS보다는 조금 느리게 동작한다.

DFS 예제
"""

from collections import deque
import sys
sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000


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


"""
2. BFS 너비 우선 탐색.

Breath-First Search.

너비 우선 탐색이라고 불리며, 쉽게 말하자면 가까운 노드부터 탐색하는 알고리즘이다.
DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식인데, BFS는 그 반대이다.
또 BFS 구현에는 DFS와 달리 큐 자료구조를 이용하는 것이 정석이고, 재귀적으로 동작하지 않는다.
인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 설계하면, 자연스럽게 먼저 들어온 것이 
먼저 나가게 되어, 가까운 노드부터 탐색을 진행할수 있기 때문이다.
DFS보다는 조금 더 빠르게 동작한다.

BFS 예제
"""


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

"""

백트래킹

Backtracking 퇴각 검색.

제약 조건 만족문제

모든 조합의 수를 살펴보는 것. 단 조건이 만족할 때 만.

해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면, 그 경로를 더이상 가지 않고, 되돌아가는 기법이다.
반복문의 횟수를 줄일 수 있어 효율적인 방법이며, 이를 가지치기라고 한다

모든 경우의 수를 탐색하는 과정에서 조건을 만들어 답이 절대로 될 수 없는 경우를 정의하고,
그러한 경우일 때 탐색을 중지한뒤 그 이전으로 돌아가 다른 경우를 탐색하는 방식으로 설계한다.

즉 백트래킹은 트리 구조를 기반으로 DFS로 탐색을 진행하면서
각 루트에 대해 조건에 부합하는지 체크,
만약 해당 조건에 맞지 않은 노드는 더 이상 탐색을 진행하지 않고, 가지를 쳐버린다.

가장 대표적인 백트래킹 문제.

백준 9663 N-Queen 문제

풀이

1 한 행에는 하나의 퀸 밖에 위치할 수 없다.(퀸은 수평 이동이 가능.)
2 맨 위에 행부터 퀸을 배치 후, 다음 행에 퀸이 이동할 수 없는 위치에 퀸을 배치한다.
3 만약 앞선 행에 위치한 퀸으로 인해, 다음 행에 해당 퀸들이 이동할 수 없는 위치가 없는 경우, 이전 행 퀸의 배치를 바꾼다.

"""


def read():
    return sys.stdin.readline().strip()


def dfs(r):
    global cnt

    if r == n:
        cnt += 1
        return
    else:
        for i in range(n):
            graph[r] = i
            if check(r):
                dfs(r+1)


def check(r):
    for i in range(r):
        if graph[r] == graph[i] or abs(graph[r] - graph[i]) == r - i:
            return False
    return True


n = int(read())
cnt = 0
graph = [0 for i in range(n)]

dfs(0)
print(cnt)
