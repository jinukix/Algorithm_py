import heapq

def solution(N, road, K):
    distance = [1e9 for i in range(N+1)]
    graph = [[] for i in range(N+1)]
    
    for a, b, c in road:
        # a -> b 비용 : c
        graph[a].append([b, c])
        graph[b].append([a, c])

    def djk(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    djk(1)

    cnt= 0
    for i in distance:
        if i <= K:
            cnt += 1

    return cnt