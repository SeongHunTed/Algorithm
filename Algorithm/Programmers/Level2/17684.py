def solution(msg):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 's', 'y', 'z']
    
    myDict = dict()
    for i in range(1, len(alphabet) + 1):
        myDict[alphabet[i-1].upper()] = i
    
    index = 0
    nextNumber = 27
    answer = []
    i = 1
    
    while True:
        while msg[index:index+i] in myDict:
            i += 1
            if index + i - 1 > len(msg):
                break
        answer.append(myDict[msg[index:index+i-1]])
        
        if index + i - 1 > len(msg):
            break
        
        if msg[index:index+i] not in myDict:
            myDict[msg[index:index+i]] = nextNumber
            nextNumber += 1
            index += i - 1
            i = 1
            
    return answer