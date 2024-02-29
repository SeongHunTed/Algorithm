import sys
sys.setrecursionlimit(10 ** 6)

global dp
dp = [-1] * 100001

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = (fibonacci(n-2) + fibonacci(n-1)) % 1234567
    return dp[n] % 1234567

def solution(n):
    answer = fibonacci(n)
    return answer

fibonacci(10)