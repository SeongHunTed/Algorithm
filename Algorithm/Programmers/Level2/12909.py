def solution(s):
    stack = []
    
    s = list(s)
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
            
    return len(stack) == 0