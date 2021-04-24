import sys
from itertools import combinations


def read():
    return sys.stdin.readline().strip()


n, m = map(int, read().split())
items = list(range(1, n + 1))
coms = list(combinations(items, m))

for com in coms:
    print(" ".join(map(str, com)))
