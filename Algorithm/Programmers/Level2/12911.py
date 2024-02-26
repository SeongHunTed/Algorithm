def solution(n):
    
    nextNumber = n
    
    while True:
        nextNumber += 1
        countOne = bin(n)[2:].count('1')
        
        if countOne == bin(nextNumber)[2:].count('1'):
            return nextNumber