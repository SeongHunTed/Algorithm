def solution(s):
    results = []
    length = len(s)
    maxCluster = length // 2
    
    for i in range(1, len(s)+1):
        std = s[0:i]
        pre = ""
        count = 1
        
        for j in range(i, len(s)+i, i):
            if std == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    pre += str(count) + std
                else:
                    pre += std
                    
                std = s[j:j+i]
                count = 1
        
        results.append(len(pre))
        
    return min(results)