import sys
input = sys.stdin.readline

n = int(input())
pack = [0] + list(map(int, input().strip().split()))
dp = [0] * 10001

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], pack[j] + dp[i-j])
    
print(dp[n])