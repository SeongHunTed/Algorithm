def solution(s):
    
    stack = []
    
    s = list(s)
    
    for char in s:
        if len(stack) != 0:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
            
    if len(stack) == 0:
        return 1
    else:
        return 0