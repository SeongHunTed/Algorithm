import sys
input = sys.stdin.readline

def whatIsTheMaxSum(n):
    dp = [0] + list(map(int, input().split()))

    for i in range(1, n+1):
        dp[i] = max(dp[i], dp[i-1] + dp[i])
    
    print(max(dp[1:]))
    

n = int(input())
whatIsTheMaxSum(n)