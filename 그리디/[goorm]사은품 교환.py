import sys

def read():
    return sys.stdin.readline()
    
t = int(read())

for _ in range(t):
    n, m = map(int, read().split())

    total = (n+m) // 12
    season = n // 5

    print(min(total, season))