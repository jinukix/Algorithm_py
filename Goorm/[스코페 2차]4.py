import sys


def read():
    return sys.stdin.readline().strip()


# n = int(read())
# char = [read() for i in range(n)]
# q = int(read())
# question = [read() for i in range(q)]

n = 5
char = ["dijkstra", "greedy", "bfs", "backtracking", "dynamic"]
q = 3
question = ["bfs", "greedyalgorithm", "ra", "g"]

for que in question:
    cnt = 0
    for ch in char:
        if que in ch:
            cnt += 1

    print(cnt)


"""

"""