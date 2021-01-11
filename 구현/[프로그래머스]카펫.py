def solution(brown, yellow):

    area = brown + yellow

    while True:
        for i in range(3, area//3 + 1):
            for j in range(3, i+1):
                if area == i*j and brown == i*2 + ((j-2) * 2) and yellow == (i-2) * (j-2):
                    return [i, j]
