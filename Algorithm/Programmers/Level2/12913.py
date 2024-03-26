# bottom-up 방식의 DP?
def solution(land):

    dp = [[-1] * 4 for _ in range(len(land))]
    dp[-1] = land[-1]
    
    for i in range(len(land)-2, -1, -1):
        for j in range(4):
            before = dp[i+1].copy()
            before[j] = -1
            dp[i][j] = max(dp[i][j], max(before) + land[i][j])
    
    return max(dp[0])