def solution(answers):
    answer = []
    answerLen = len(answers)
    n1 = answerLen // 5 + 1
    n2 = answerLen // 8 + 1
    n3 = answerLen // 10 + 1
    
    person1 = [1, 2, 3, 4, 5] * n1
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] * n2
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * n3
    
    count1, count2, count3 = 0, 0, 0
    
    for i in range(answerLen):
        if person1[i] == answers[i]: count1 += 1
        if person2[i] == answers[i]: count2 += 1
        if person3[i] == answers[i]: count3 += 1
        
    rank = [count1, count2, count3]
    maxScore = max(rank)
    
    for i in range(1, 4):
        if rank[i-1] == maxScore:
            answer.append(i)
    
    return answer