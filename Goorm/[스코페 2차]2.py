import sys


def read():
    return sys.stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(read())
resource = [list(read().split()) for i in range(n)]
country = set()

for i in resource:
    country.add(i[0])
    country.add(i[1])

country = list(country)
parent = [0 for i in range(n)]
edges = []

for i in range(n):
    parent[i] = i

for i in resource:
    c = int(i[2])
    a = country.index(i[0])
    b = country.index(i[1])
    edges.append([c, a, b])

edges.sort()
ans = 0

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += c

print(ans)


"""
a - b 10
b - c 2
c - a 7

다 연결 최소 비용?
"""