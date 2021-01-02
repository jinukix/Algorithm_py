import heapq


def solution(jobs):

    cnt, ans, end = 0, 0, -1
    heap = []
    jobs.sort()
    start = jobs[0][0]

    while len(jobs) != cnt:

        for s, t in jobs:
            if end < s <= start:
                heapq.heappush(heap, (t, s))

        if heap:
            t, s = heapq.heappop(heap)
            end = start
            start += t
            ans += start-s
            cnt += 1
        else:
            start += 1

    return ans // len(jobs)
