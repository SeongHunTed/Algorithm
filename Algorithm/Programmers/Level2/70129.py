def solution(s):
    
    zeroCount = 0
    changeCount = 0
    result = []
    
    while True:
        
        if s == '1':
            return [changeCount, zeroCount]
        
        zeroCount += s.count('0')
        s = s.replace('0', '')
        
        length = len(s)
        s = bin(length)[2:]
        print(bin(length))
        
        changeCount += 1
        