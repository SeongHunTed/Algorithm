import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]

for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[-1])
    exit()

dp = [[0] * (3) for _ in range(n+1)]

dp[1][1] = stairs[1]
dp[1][2] = 0
dp[2][1] = stairs[2]
dp[2][2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stairs[i]
    dp[i][2] = dp[i-1][1] + stairs[i]

print(max(dp[n][1], dp[n][2]))