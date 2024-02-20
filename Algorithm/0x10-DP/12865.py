import sys
input = sys.stdin.readline

n, k = map(int, input().split())

stuffs = []
for _ in range(n):
    stuffs.append(list(map(int, input().split())))

dp = [[0] * (k+1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = stuffs[i-1][0], stuffs[i-1][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j - weight])

print(max(dp[n]))