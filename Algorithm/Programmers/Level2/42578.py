def solution(clothes):
    
    myCloth = {}
    for i in range(len(clothes)):
        if clothes[i][1] in myCloth:
            myCloth[clothes[i][1]] += 1
        else:
            myCloth[clothes[i][1]] = 1
    
    count = 1
    for key in myCloth:
        count = count * (myCloth[key] + 1)
        
    return count - 1
    