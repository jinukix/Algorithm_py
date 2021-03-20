import sys

def read():
    return sys.stdin.readline()

def calCount(arr):
    if not arr:
        return 0

    if len(arr) <= 2:
        return max(arr)

    minVal = min(arr)
    minIdx = arr.index(minVal)

    cnt = minVal
    cnt += max(0, calCount(arr[:minIdx]) - minVal)
    cnt += max(0, calCount(arr[minIdx+1:]) - minVal)

    return cnt


n = int(read())
tabs = [list(map(int, read().split())) for i in range(2)]

diff = []
for a, b in zip(tabs[0], tabs[1]):
    diff.append(a-b)

ans = 0
prev_plus = diff[0] > 0
arr = []
for i in diff:
    now_plus = i > 0 

    if prev_plus == now_plus:
        arr.append(abs(i))
    else:
        ans += calCount(arr)
        arr = []
        arr.append(abs(i))
        prev_plus = now_plus

ans += calCount(arr)

print(ans)