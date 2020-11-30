"""
정렬

정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는것을 의미한다.

프로그램에서 데이터를 가공할 때 오름차순이나 내림차순 등 어떤 식으로든 정렬해서
사용하는 경우가 많기에 가장 기본이되는 알고리즘이라고 말할 수 있다.

선택정렬.

데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택하는 알고리즘으로 가장 원시적인 방법이다.

단순히 가장 작은 데이터를 선택해 맨 앞에 데이터와 바꾸고,
그다음 작은데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복한다.

선택정렬 예제

"""

array = [7, 5, 2, 8, 1, 9, 0, 4, 3, 6]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
# 결과
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
삽입정렬

데이터를 하나씩 확인하여, 각 데이터를 적절한 위치에 삽입하는 알고리즘이다.

삽입 정렬은 두 번째 인덱스부터 시작한다.
(첫 번째 인덱스는 그 자체로 정렬되어 있다고 판단.)

1. 두 번째 인덱스부터 기준으로 삼아 현재 인덱스-1와 비교 한다.
2. 기준으로 잡은 데이터가 더 작을 경우 두 값을 바꿔주고 다시 비교한 인덱스-1 와 비교 해준다
3. 자기보다 더 작은 데이터를 만났을 경우 그 위치에서 멈춘다.

삽입정렬 예제
"""

array = [7, 5, 2, 8, 1, 9, 0, 4, 3, 6]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
# 결과
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
# 퀵 정렬

퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.
특징으로는 피벗(pivot)이 사용되며 큰 숫자와 작은 숫자를 비교할 때,
교환하기 위한 '기준'을 피벗이라 한다.

리스트에서 첫 번째 데이터를 피벗으로 설정한다.
왼쪽에서는 피벗보다 큰 데이터를 찾고,
오른쪽에서는 피벗보다 작은 데이터를 찾는다.
엇갈리지 않았다면 두 값의 위치를 교환하고 엇갈릴때 까지 위 과정을 반복한다.
두 값의 위치가 엇갈렸다면 작은 데이터와 피벗의 위치를 교환하고
피벗의 위치를 고정시키고 피벗의 위치를 기준으로 왼쪽, 오른쪽리스트를 분할한다.
이러한 상태에서 왼쪽, 오른쪽 리스트를 개별적으로 위 과정을 수행해주면 된다.

퀵 정렬 예제
"""
array = [7, 5, 2, 8, 1, 9, 0, 4, 3, 6]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개 인 경우 break
        return

    pivot = start  # 첫 번째 원소를 피벗으로 설정한다.
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)
# 결과
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
