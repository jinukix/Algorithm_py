from collections import deque

def solution(cacheSize, cities):
    ans = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()

        # hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            ans += 1
        
        # miss
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            ans += 5

    return ans