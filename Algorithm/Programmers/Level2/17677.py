def makeWord(string):
    data = []
    for i in range(len(string) - 1):
        if string[i].isalpha() and string[i+1].isalpha(): 
            data.append(string[i:i+2].upper())
    return data

def solution(str1, str2):
    answer = 0
    data1 = makeWord(str1) 
    data2 = makeWord(str2)

    union = set(data1) | set(data2)
    intersection = set(data1) & set(data2)
    
    if not union: return 65536
    
    unionCount = 0
    intersectionCount = 0
    
    for item in union:
        unionCount += max(data1.count(item), data2.count(item))
        
    for item in intersection:
        intersectionCount += min(data1.count(item), data2.count(item))
    
    return int(intersectionCount / unionCount * 65536)