import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def fibonacci(number):
    for i in range(2, number+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[number]
    

n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
print(fibonacci(n))