"""
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
