import sys
from collections import Counter


def read():
    return sys.stdin.readline().strip()


s = read().upper()
counter = Counter(s).most_common()

if len(counter) >= 2 and counter[0][1] == counter[1][1]:
    print("?")
else:
    print(counter[0][0])