from collections import deque
def solution(cacheSize, cities):
    cacheHit = 1
    cacheMiss = 5
    cache = deque()
    count = 0
    
    if cacheSize == 0:
        return len(cities) * cacheMiss
    
    for city in cities:
        city = city.lower()
        if city in cache:
            count += cacheHit
            cache.remove(city)
            cache.append(city)
        else:
            count += cacheMiss
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(city)
            else:
                cache.append(city)
                
    return count