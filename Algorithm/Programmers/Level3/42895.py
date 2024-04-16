def solution(N, number):
    dp = [set() for _ in range(9)]
    
    if N == number: return 1
    else: dp[1] = {N}

    for i in range(2, 9):
        result = {int(str(N) * i)}
        
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    result.add(num1 + num2)
                    result.add(num1 - num2)
                    result.add(num1 * num2)
                    result.add(num1 // num2)
        
        result.remove(0)
        if number in result:
            return i
        dp[i] = result
        
    return -1