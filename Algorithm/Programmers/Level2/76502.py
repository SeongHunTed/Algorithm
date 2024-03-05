def isRight(s):
    parenStack = []
    
    for char in s:
        if char == ')' and len(parenStack) > 0 and parenStack[-1] == '(':
            parenStack.pop()
        elif char == '}' and len(parenStack) > 0 and parenStack[-1] == '{':
            parenStack.pop()
        elif char == ']' and len(parenStack) > 0 and parenStack[-1] == '[':
            parenStack.pop()
        elif char == '(':
            parenStack.append(char)
        elif char == '{':
            parenStack.append(char)
        elif char == '[':
            parenStack.append(char)
        else:
            return False
    
    if len(parenStack) == 0:
        return True
    else:
        return False
            

def solution(s):
    result = 0
    for i in range(len(s)):
        newS = s[i:] + s[:i]
        if isRight(newS):
            result += 1
            
    return result
        
        