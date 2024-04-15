import sys
input = sys.stdin.readline

n, testCase = map(int, (input().split(" ")))
dp = [0] + list(map(int, input().split(" ")))

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i]

for _ in range(testCase):
    start, end = map(int, input().split(" "))
    print(dp[end]-dp[start-1])