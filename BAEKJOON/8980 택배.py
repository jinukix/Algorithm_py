"""
정말 오래걸렸던 문제이다.
처음에는 시작하는 마을, 도착하는 마을순서를 기준으로 정렬을 해 풀었으나
반례를 찾지못하고 제출할때 마다 이게 왜 틀리다는 것이냐! 라며 많이 헤맸던 문제이다.
결론을 말하자면 도착하는 마을을 기준으로 정렬 해주어야하는 문제였다.
이 문제를 풀면서 그리디문제는 어떤 것을 기준으로 삼고 어떤 순서대로 정렬해 푸는것이 중요하다는것을 다시 한번 깨닫는 문제였던 것 같다.

일단 도착점을 제외한 마을에서의 실을 수 있는 무게를 생각하여야한다.
1. 도착점을 제외한 마을의 c만큼 부여해준다.
2. 도착하는 마을을 기준으로 짐들을 정렬해 준다.
3-1. 해당 짐의 출발지 ~ 도착지-1 까지 마을의 실릴 무게중 가장 적은 곳을 찾는다.
3-2. 2에서 찾은 무게와 해당 짐의 무게를 비교해 실을 수 있을 만큼 실는다.
3-3. 실은만큼의 무게를 해당 짐의 출발지 ~ 도착지-1 까지 마을 실을 무게를 빼준다.

3을 계속 반복해주면 된다.
"""

import sys

def read():
    return sys.stdin.readline().strip()

n, c = map(int, read().split())
m = int(read())

village = [c for i in range(n-1)]

data = []

for i in range(m):
    a, b, c = map(int, read().split())
    data.append([a, b, c])

data.sort(key=lambda x: x[1])

min_index = 0
min_w = 0
ans = 0

for i in range(m):
    min_w = village[data[i][0]-1]
    for j in range(data[i][0], data[i][1]):
        if min_w >= village[j-1]:
            min_w = village[j-1]
            min_index = j-1

    w = 0
    if village[min_index] >= data[i][2]:
        w = data[i][2]
    elif village[min_index] > 0:
        w = village[min_index]

    if w > 0:
        for j in range(data[i][0], data[i][1]):
            village[j-1] -= w
        ans += w

print(ans)
