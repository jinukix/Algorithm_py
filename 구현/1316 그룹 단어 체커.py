import sys


def read():
    return sys.stdin.readline()


n = int(read())
cnt = 0


for i in range(n):
    word = read()
    for j in range(len(word)):
        if j != len(word)-1:  # 공백의 경우. j+1과 비교 하므로 공백 일부러 제거안하고 예외처리.
            # word[j]가 word[j+1]랑 다르면서 뒤에 존재하는 경우.
            if word[j] != word[j+1] and word[j] in word[j+1:]:
                break
        else:  # 문자의 끝까지 도달.
            cnt += 1

print(cnt)
