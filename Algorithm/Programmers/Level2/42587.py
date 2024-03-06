from collections import deque

def solution(priorities, location):
    q = deque()
    count = 0
    
    myPriority = list()
    
    for i in range(len(priorities)):
        if i == location:
            q.append((priorities[i], True))
        else:
            q.append((priorities[i], False))
        myPriority.append(priorities[i])
        
    myPriority.sort(reverse=True)
    index = 0
    
    while q:
        maxPriority = myPriority[index]
        priority, isTarget = q.popleft()
        
        if priority == maxPriority:
            count += 1
            index += 1
            if isTarget:
                return count
        else:
            q.append((priority, isTarget))    
            
    return count
    