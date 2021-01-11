import heapq


def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0

    while scoville:

        if scoville[0] >= K:
            return cnt

        if len(scoville) < 2:
            return -1

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        heapq.heappush(scoville, a+(b*2))

        cnt += 1


scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))
