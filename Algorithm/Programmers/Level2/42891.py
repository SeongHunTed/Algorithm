from collections import deque

def solution(food_times, k):

    q = deque([i for i in range(1, len(food_times)+1)])
    
    # 음식 잔여량 딕셔너리
    foodLeft = {}
    for i in range(1, len(food_times)+1):
        foodLeft[i] = food_times[i-1]
    
    second = 0
    # 1초부터 k초까지 진행
    while True:
        
        # stop 조건
        if second == k:
            break
        if len(q) == 0:
            break
        
        food = q.popleft()
        
        if foodLeft[food] != 0:
            foodLeft[food] -= 1
            second += 1
            if foodLeft[food] == 0: continue
            q.append(food)
            
    
    if len(q) > 0:
        return q.popleft()
    else:
        return -1
            
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    foodheap = []
    length = len(food_times)
    
    for i in range(length):
        heapq.heappush(foodheap, [food_times[i], i+1])
    
    time = 0
    while (foodheap[0][0] - time) * length < k:
        k -= (foodheap[0][0] - time) * length
        time += (foodheap[0][0] - time)
        length -= 1
        heapq.heappop(foodheap)
        
    result = sorted(foodheap, key=lambda x: x[1])
    answer = result[k % length][1]
    
    return answer
