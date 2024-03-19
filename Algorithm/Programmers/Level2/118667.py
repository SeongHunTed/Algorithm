from collections import deque

def solution(queue1, queue2):
    answer = 0
    leftSum = sum(queue1)
    rightSum = sum(queue2)
    
    left = deque(queue1)
    right = deque(queue2)
    
    if (leftSum + rightSum) % 2 != 0:
        return -1

    while True:
        if answer == 4 * len(queue1):
            return -1
        
        if leftSum > rightSum:
            value = left.popleft()
            right.append(value)
            leftSum -= value
            rightSum += value
        elif leftSum < rightSum:
            value = right.popleft()
            left.append(value)
            leftSum += value
            rightSum -= value
        else:
            return answer
        
        answer += 1
        
    return answer