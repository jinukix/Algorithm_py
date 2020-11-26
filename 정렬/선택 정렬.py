"""
선택정렬.

데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택하는 알고리즘으로 가장 원시적인 방법이다.

단순히 가장 작은 데이터를 선택해 맨 앞에 데이터와 바꾸고,
그다음 작은데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복한다.
"""

array = [7, 5, 2, 8, 1, 9, 0, 4, 3, 6]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # swap

print(array)
# 결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
