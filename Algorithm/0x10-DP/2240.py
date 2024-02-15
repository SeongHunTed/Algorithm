import sys
input = sys.stdin.readline

jadoo = 1
time, w = map(int, input().split())

plumSequence = [0]
for _ in range(time):
    plumSequence.append(int(input()))
dp = [[0] * (w + 1) for _ in range(time+1)]

for i in range(1, time+1):

    if plumSequence[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, w+1):
        if plumSequence[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif plumSequence[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[time]))