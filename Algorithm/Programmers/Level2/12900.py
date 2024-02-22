import sys
sys.setrecursionlimit(10 ** 6)

global dp
dp = [0] + [-1] * 60000

def recursion(n):
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = recursion(n-1) + recursion(n-2)
    
    return dp[n] % 1000000007
    

def solution(n):
    dp[1] = 1
    dp[2] = 2
    answer = recursion(n)
    return answer