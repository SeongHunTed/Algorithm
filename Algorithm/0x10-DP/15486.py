import sys
input = sys.stdin.readline

n = int(input())
counsel = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

M = 0
for i in range(n):
    M = max(M, dp[i])
    if i + counsel[i][0] > n:
        continue
    dp[i+counsel[i][0]] = max(M+counsel[i][1], dp[i+counsel[i][0]])

print(max(dp))