"""
백트래킹.

Backtracking 퇴각 검색.

제약 조건 만족문제

모든 조합의 수를 살펴보는 것. 단 조건이 만족할 때 만.

해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면, 그 경로를 더이상 가지 않고, 되돌아가는 기법이다.
반복문의 횟수를 줄일 수 있어 효율적인 방법이며, 이를 가지치기라고 한다

모든 경우의 수를 탐색하는 과정에서 조건을 만들어 답이 절대로 될 수 없는 경우를 정의하고,
그러한 경우일 때 탐색을 중지한뒤 그 이전으로 돌아가 다른 경우를 탐색하는 방식으로 설계한다.

즉 백트래킹은 트리 구조를 기반으로 DFS로 탐색을 진행하면서
각 루트에 대해 조건에 부합하는지 체크,
만약 해당 조건에 맞지 않은 노드는 더 이상 탐색을 진행하지 않고,
가지를 쳐버린다.


가장 대표적인 백트래킹 문제.

백준 9663 N-Queen 문제

풀이

1 한 행에는 하나의 퀸 밖에 위치할 수 없다.(퀸은 수평 이동이 가능.)
2 맨 위에 행부터 퀸을 배치 후, 다음 행에 퀸이 이동할 수 없는 위치에 퀸을 배치한다.
3 만약 앞선 행에 위치한 퀸으로 인해, 다음 행에 해당 퀸들이 이동할 수 없는 위치가 없는 경우, 이전 행 퀸의 배치를 바꾼다.


"""


import sys


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


# ~~~
