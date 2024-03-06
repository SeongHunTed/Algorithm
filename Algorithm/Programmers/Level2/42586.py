def solution(progresses, speeds):
    
    result = []
    
    while speeds:
        
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed
            
        count = 0
        
        while progresses and progresses[0] >= 100:
            del progresses[0], speeds[0]
            count += 1
            
        if count > 0:
            result.append(count)
            
    return result