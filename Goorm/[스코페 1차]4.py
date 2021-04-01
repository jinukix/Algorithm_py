import sys


def read():
    return sys.stdin.readline().strip()


s = list(map(float, read().split()))
# s = [4.01111, 3.11241240, 2.1, 4.3, 5.0]
n, m = map(int, read().split())
genre = [read() for i in range(n)]
info = [read() for i in range(n)]

alpha = []

for i, a in zip(range(len(s)), ["A", "B", "C", "D", "E"]):
    s[i] = [s[i], a]

s.sort(reverse=True)

dict1 = {}
score = ""
for i in s:
    dict1[i[1]] = format(i[0], ".1f")
    score += i[1]

# n = 2
# m = 3
# genre = ['WYO', 'YYO']
# info = ['ABC', 'DCE']

dict = {}
dict["Y"] = []
dict["O"] = []
dict["W"] = []

for i in range(n):
    for j in range(m):
        dict[genre[i][j]].append([info[i][j], dict1[info[i][j]], i, j])

ans1 = []
ans2 = []

for i in dict["O"]:
    ans2.append(i)

for i in dict["Y"]:
    ans1.append(i)

ans1.sort(key=lambda x: score.index(x[0]))
ans2.sort(key=lambda x: score.index(x[0]))
ans1.extend(ans2)

for i in ans1:
    ans = f"{i[0]} {i[1]} {i[2]} {i[3]}"
    print(ans)


"""
안 본 컨텐츠 없게 해줘 이벤트

장르 선호도 0.0 <= 5.0 소숫점 첫째자리 까지

1. 열람한 적 없는 컨텐츠를 선호도 높은 순서대로 추천
2. 유저가 열람했으나 끝까지 다 보지 못한 컨텐츠는 장르 선호도가 높은 컨텐츠 순서대로 추천

무작위 순서 n * m 만큼 컨텐츠 나열

O : 열람 했으나 끝까진 보지 않음
W : 열람 했고 끝까지 봄
Y : 유저가 열람한 적 없음

장르는 A B C D E






4.0 3.0 2.1 4.3 5.0
2 3
WYO
YYO
ABC
DCE





"""