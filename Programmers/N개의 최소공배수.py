from math import gcd

def solution(arr):

    while arr:
        if len(arr) == 1:
            break

        num1 = arr.pop()
        num2 = arr.pop()
        g = gcd(num1, num2)
        arr.append((num1 * num2) // g)

    return arr[0]