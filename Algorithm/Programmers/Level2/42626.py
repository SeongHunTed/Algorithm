import heapq as hp

def solution(scoville, K):
    answer = 0
    scoville.sort()
    hp.heapify(scoville)
    
    while scoville[0] < K:
        answer += 1
        first = hp.heappop(scoville)
        second = hp.heappop(scoville)
        newOne = first + 2 * second
        
        hp.heappush(scoville, newOne)
        
        if len(scoville) == 2 and scoville[0] + 2 * scoville[1] < K:
            return -1
        
    return answer