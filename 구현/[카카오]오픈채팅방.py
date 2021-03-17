def solution(record):
    dict = {}
    ans = []

    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter' or r[0] == 'Change':
            dict[r[1]] = r[2]

    for i in range(len(record)):
        r = record[i].split(" ")

        if r[0] == 'Enter':
            ans.append(dict[r[1]] + "님이 들어왔습니다.")

        elif r[0] == 'Leave':
            ans.append(dict[r[1]] + "님이 나갔습니다.")

    return ans