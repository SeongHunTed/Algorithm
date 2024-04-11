def solution(s):
    answer = 999999
    maxSplit = len(s) // 2 + 1
    
    if len(s) == 1:
        return 1

    for i in range(1, maxSplit):
        index = 0
        result = ""
        stack = []
        beforeText = s[:i]
        
        while True:
            index += 1
            
            if index > len(s) // i:
                result += s[i*(index-1):]
                break
            nextText = s[i*index:i*(index+1)]

            if beforeText == nextText:
                stack.append(beforeText)
            else:
                if len(stack) != 0:
                    result += str(len(stack) + 1) + stack[-1]
                    stack = []
                else:
                    result += beforeText
            
            beforeText = nextText
            
        answer = min(answer, len(result))
            
    return answer
    