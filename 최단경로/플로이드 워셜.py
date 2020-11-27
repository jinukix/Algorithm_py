"""
다익스트라 알고리즘이 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘이였다면,
플로이드 워셜 알고리즘은 **모든 지점에서 다른 모든 지점까지의 최단 경로**를 구하는 알고리즘이다.

다익스트라는 단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택해, 해당 노드를 거쳐 가는 경로를 확인하며,
테이블을 갱신하는 방식으로 동작한다, 플로이드 워셜 알고리즘 또한 단계마다 '거쳐 가는 노드'를 기준으로 알고리즘을 수행한다.
하지만 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다는 점에서 차이가 있다.

"""
import sys

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

for k in range(1, n+1): # 경로가 가장 상단이여야 한다
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
