def solution(order):
    answer = 0
    subContainer = []
    index = 0
    box = 1
    
    while True:
        if index >= len(order):
            break
            
        if box > len(order):
            if order[index] != subContainer[-1]:
                break
        
        if box == order[index]:
            answer += 1
            index += 1
            box += 1
        elif len(subContainer) > 0 and subContainer[-1] == order[index]:
            subContainer.pop()
            answer += 1
            index += 1
        else:
            subContainer.append(box)
            box += 1
        
    return answer