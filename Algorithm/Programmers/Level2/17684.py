def solution(msg):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    myDict = dict()
    for i in range(1, len(alphabet) + 1):
        myDict[alphabet[i-1].upper()] = i
    
    l = 0
    r = 1
    value = 27
    answer = []
    
    while True:
        if r > len(msg):
            if msg[l:] in myDict:
                answer.append(myDict[msg[l:]])
            break
        key = msg[l:r]
        
        if key in myDict:
            r += 1
            continue
        else:
            answer.append(myDict[msg[l:r-1]])
            myDict[key] = value
            value += 1
            l = r - 1
            r = l + 1

    return answer