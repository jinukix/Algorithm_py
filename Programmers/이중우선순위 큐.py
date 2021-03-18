import heapq


def changeheap(heap):
    h = []
    for i in heap:
        heapq.heappush(h, -i)
    return h


def solution(operations):

    min_heap = []
    max_heap = []

    for i in operations:

        if i[0] == "I":
            n = int(i[2:])
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            # print(f"{n} 추가")
        else:
            try:
                if i[-2] != '-':
                    heapq.heappop(max_heap)
                    min_heap = changeheap(max_heap)
                else:
                    heapq.heappop(min_heap)
                    max_heap = changeheap(min_heap)
            except:
                pass

    if len(min_heap) == 0:
        return [0, 0]
    else:
        min_n = heapq.heappop(min_heap)
        print(min_n)
        max_heap = changeheap(min_heap)
        max_n = heapq.heappop(max_heap)
        return [-max_n, min_n]


operations = ["I -45", "I 653", "D 1", "I -642",
              "I 45", "I 97", "D 1", "D -1", "I 333"]

print(solution(operations))
