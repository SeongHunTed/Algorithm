# testCase 일부만 통과
def solution(arr):
    dp = [[] for _ in range(len(arr) // 2 + 1)]
    dp[0] = [arr]
    results = []
    
    # 연산자 개수 만큼 반복
    for i in range(1, len(arr) // 2 + 1):
        
        # dp[i-1]에 있는 후보 개수만큼 진행
        for item in dp[i-1]:
            length = len(item) # 9
            candidate = []
            values = []
        
            for j in range(0, length - 2, 2):
                value = 0
                result = []
                if item[j+1] == "+":
                    value = int(item[j]) + int(item[j+2])
                else:
                    value = int(item[j]) - int(item[j+2])
                    
                values.append(value)
                
                if j == 0:
                    result = [str(value)] + item[j+3:]
                elif j == length - 2:
                    result = item[:j] + [str(value)]
                else:
                    result = item[:j] + [str(value)] + item[j+3:]
                    
                candidate.append(result)
                
            maxIndex = values.index(max(values))
            minIndex = values.index(min(values))
            dp[i].append(candidate[maxIndex])
            dp[i].append(candidate[minIndex])
            

    candidates = dp[-1]
    for item in candidates:
        results.append(int(item[0]))
        
    return max(results)