"""
퀵 정렬

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
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
profile
