def solution(s):
    tuples = []
    s = s.lstrip("{{")
    s = s.rstrip("}}")
    s = list(s.split("},{"))
    
    for item in s:
        newString = list(item.split(","))
        newList = list(map(int, newString))
        tuples.append(newList)
    
    tuples.sort(key=lambda x : len(x))
    
    answer = []
    for tuple in tuples:
        if len(tuple) == 1:
            answer.append(tuple[0])
        else:
            for item in tuple:
                if item not in answer:
                    answer.append(item)
                    
    return answer