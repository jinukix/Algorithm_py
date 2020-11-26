"""
우선순위 큐를 2가지 사용해 푼 문제이다.
1. 강의가 시작하는 기준으로 우선순위 큐(pq)에 담는다.
2. 다른 우선순위 큐(rooms)에 가장 빨리 끝나는 강의시간을 넣는다.
3. pq가 빌때 까지 다음 연산을 반복한다.

4-1. pq에서 강의를 꺼내 강의가 시작하는 시간과 rooms에 있는 가장 빨리 끝나는 강의시간을 비교한다.
4-2. 강의가 시작하는 시간이 더 빠르다면 강의실을 추가한다.
4-3. 강의가 시작이 시간이 더 늦다면 해당 끝나는 강의시간을 pop해준다.
4-4. pq에서 꺼낸 강의의 끝나는 시간을 rooms에 넣어준다.

"""

import sys
import heapq

read = sys.stdin.readline


n = int(read())

pq = []
rooms = []
cnt = 1

for _ in range(n):
    a, b = map(int, read().split())
    heapq.heappush(pq, [a, b])

heapq.heappush(rooms, heapq.heappop(pq)[1])

while pq:
    currentRoom = heapq.heappop(pq)
    if currentRoom[0] < rooms[0]:
        cnt += 1
    else:
        heapq.heappop(rooms)
    heapq.heappush(rooms, currentRoom[1])

print(cnt)
