import sys
input = sys.stdin.readline

numberOfStair = int(input())
stair = [0] + [int(input()) for _ in range(numberOfStair)]
dp = [0] * (numberOfStair+1)

for i in range(1, numberOfStair+1):
    if i == 1: dp[1] = stair[1]
    elif i == 2: dp[2] = stair[1] + stair[2]
    elif i == 3: dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])
    else: dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])

print(dp[numberOfStair])