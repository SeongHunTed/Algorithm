def isRightString(string):
    stack = []
    
    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
            
    return len(stack) == 0

def splitToBalancedString(string):
    balance = 0
    for index, char in enumerate(string):
        if char == "(":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            return (string[:index+1], string[index+1:])

def solution(p):
    if len(p) == 0 or isRightString(p):
        return p
    
    u, v = splitToBalancedString(p)
    
    if isRightString(u):
        return u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        for char in u[1:-1]:
            if char == "(":
                answer += ")"
            else:
                answer += "("
        return answer
            