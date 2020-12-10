import sys


def read():
    return sys.stdin.readline().strip()


t = int(read())


for _ in range(t):
    n = int(read())
    n_set = set(map(int, read().split()))

    m = int(read())
    m_set = list(map(int, read().split()))

    for i in m_set:
        if i in n_set:
            print(1)
        else:
            print(0)
