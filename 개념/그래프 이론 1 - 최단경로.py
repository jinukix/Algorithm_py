"""

그래프

그래프란 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조를 의미한다.
알고리즘 문제를 접했을 때 '서로 다른 개체'가 연결되어 있다는 이야기를 들으면
가장 먼저 그래프 알고리즘을 떠올려야 한다.

최단경로 

최단경로 알고리즘은 말 그래도 가장 짧은 경로를 찾는 알고리즘이다.
그래서 '길 찾기'문제라고도 불린다.
대표적인 최단경로 알고리즘으로는 다익스트라와 플로이드 워셜을 꼽을 수 있다


1. 다익스트라 알고리즘

다익스트라 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 
특정한 노드에서 출발하여 다른 노드로 가는 **각각의 최단 경로**를 구해주는 알고리즘이다.
음의 간선이 존재하지 않을 때 정상적으로 작동이 된다.

다익스트라 알고리즘은 그리디, DP의 한 유형으로 볼 수있는데 
다익스트라는 하나의 최단 거리를 구할 때 그 이전까지 구했던 최단 거리 정보를 그대로 사용한다는 특징이있기 때문이다.

1. 출발 노드 설정.
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산 해 테이블 갱신.
5. 3~4 반복.

다익스트라 예제
"""

import heapq
import sys

INF = 1e9


def read():
    return sys.stdin.readline().strip()


def djk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:  # 현재 노드가 처리된 적이 있다면 무시
            continue

        for i in graph[now]:  # 현재 노드와 연결된 노드들 확인.
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m = map(int, read().split())  # 노드, 간선의 개수.
start = int(read())
graph = [[] for i in range(n+1)]
distance = [INF for i in range(n+1)]

# 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, read().split())
    # a -> b 비용 : c
    graph[a].append([b, c])

djk(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF", end=" ")
    else:
        print(distance[i], end=" ")

"""

입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력
0 2 3 1 2 4
"""


"""

2. 플로이드 워셜 알고리즘

다익스트라 알고리즘이 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘이였다면,
플로이드 워셜 알고리즘은 **모든 지점에서 다른 모든 지점까지의 최단 경로**를 구하는 알고리즘이다.

다익스트라는 단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택해, 해당 노드를 거쳐 가는 경로를 확인하며,
테이블을 갱신하는 방식으로 동작한다, 플로이드 워셜 알고리즘 또한 단계마다 '거쳐 가는 노드'를 기준으로 알고리즘을 수행한다.
하지만 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다는 점에서 차이가 있다.

플로이드 워셜 알고리즘 예제
"""


INF = 1e9


def read():
    return sys.stdin.readline().strip()


n = int(read())
m = int(read())

graph = [[INF for i in range(n+1)] for i in range(n+1)]

# 자기 자신에가 가는 비용은 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, read().split())
    # a->b 비용 : c
    graph[a][b] = c

for k in range(1, n+1):  # 경로가 가장 상단이여야 한다
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
"""

입력
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
"""
