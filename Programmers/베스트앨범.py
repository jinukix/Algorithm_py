from collections import defaultdict


def solution(genres, plays):

    cnt_dict = defaultdict(int)
    dict = defaultdict(list)
    cnt = 0

    for g, p in zip(genres, plays):
        cnt_dict[g] += p
        dict[g].append([cnt, p])
        cnt += 1

    cnt_dict_order = sorted(
        cnt_dict.keys(), key=lambda x: cnt_dict[x], reverse=True)

    print(dict)
    ans = []
    print(dict["pop"])
    for i in cnt_dict_order:
        print(i)
        ans.extend([n for n, p in sorted(
            dict[i], key=lambda x:x[1], reverse=True)[:2]])

    return ans


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))


# dict["classic"] = {1: 500, 3: 150}
