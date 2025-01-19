from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    cities = [city.lower() for city in cities]  # 대소문자 구분 없이 처리
    
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1  # Cache hit
        else:
            cache.append(city)
            answer += 5  # Cache miss

    return answer