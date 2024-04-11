def solution(s):
    answer = len(s)
    
    for length in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:length]
        count = 1
        
        for i in range(length, len(s), length):
            current = s[i:i+length]
            
            if prev == current:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                
                prev = current
                count = 1
                
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
            
        answer = min(len(compressed), answer)
    
    return answer