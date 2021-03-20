import sys

def read():
    return sys.stdin.readline().strip()

s = read()

ans = [0, 0]
prev = s[0] == '0'

for i in s:
    now = i == '0'

    if prev != now:
        ans[int(now)] += 1
        prev = now

ans[int(s[-1])] +=1 

print(min(ans))