def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    strA = []
    strB = []

    for i in range(len(str1)-1):
        if (str1[i] + str1[i+1]).isalpha():
            strA.append(str1[i] + str1[i+1])
    
    for i in range(len(str2)-1):
        if (str2[i] + str2[i+1]).isalpha():
            strB.append(str2[i] + str2[i+1])

    if len(strA) > len(strB):
        inter = [strA.remove(i) for i in strB if i in strA]
    else:
        inter = [strB.remove(i) for i in strA if i in strB]

    uni = strA + strB

    if not uni:
        return 65536

    return int((len(inter) / len(uni)) * 65536)