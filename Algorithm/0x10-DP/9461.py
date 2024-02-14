import sys
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    n = int(input())
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * (n-9)

    if n > 10:
        for i in range(11, n+1):
            dp[i] = dp[i-2] + dp[i-3]

    print(dp[n])
