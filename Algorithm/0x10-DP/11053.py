import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))