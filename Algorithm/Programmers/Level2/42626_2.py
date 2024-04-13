import heapq as hp

def solution(scoville, K):
    food = []
    for scovil in scoville:
        hp.heappush(food, scovil)
    count = 0
    
    while True:
        if len(food) == 1:
            if food[0] >= K:
                return count
            else:
                return -1
        
        first = hp.heappop(food)
        
        if first >= K:
            break
        
        second = hp.heappop(food)
        mix = first + second * 2
        hp.heappush(food, mix)
        count += 1
    
    return count