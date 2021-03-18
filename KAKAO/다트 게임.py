def solution(dartResult):

    ans = 0
    num1, num2 = 0, 0
    for i in range(len(dartResult)):

        if dartResult[i] == "S":
            ans += num1
            num1 = num2

            if dartResult[i-2]+dartResult[i-1] == '10':
                num2 = 10
            else:
                num2 = int(dartResult[i-1])

        elif dartResult[i] == "D":
            ans += num1
            num1 = num2

            if dartResult[i-2]+dartResult[i-1] == '10':
                num2 = 10
            else:
                num2 = int(dartResult[i-1])
            num2 **= 2

        elif dartResult[i] == "T":
            ans += num1
            num1 = num2

            if dartResult[i-2]+dartResult[i-1] == '10':
                num2 = 10
            else:
                num2 = int(dartResult[i-1])
            num2 **= 3

        elif dartResult[i] == "*":
            num1 *= 2
            num2 *= 2

        elif dartResult[i] == "#":
            num2 *= -1

    ans += num1+num2
    return ans


dartResult = "1D2S#10S"
print(solution(dartResult))
