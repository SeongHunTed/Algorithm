def solution(k, tangerine):
    
    answer = 0
    myDict = dict()
    
    for one in tangerine:
        if one in myDict:
            myDict[one] += 1
        else:
            myDict[one] = 1
    
    sortedNumber = sorted(myDict.items(), key=lambda x : x[1], reverse=True)
    
    for i in range(len(sortedNumber)):
        k -= sortedNumber[i][1]
        answer += 1
        if k <= 0: break
        
    return answer
