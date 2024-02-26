def solution(n):
    count = 0
    
    for i in range(1, n//2 + 1):
        sumation = 0
        for j in range(i, n+1):
            sumation += j
            if sumation == n:
                count += 1
                break
            elif sumation > n:
                break
                
    return count + 1