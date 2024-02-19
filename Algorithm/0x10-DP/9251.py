import sys
input = sys.stdin.readline

a = [''] + list(input().rstrip())
b = [''] + list(input().rstrip())

lenA = len(a)
lenB = len(b)

dp = [[0] * (lenB) for _ in range(lenA)]

for i in range(1, lenA):
    for j in range(1, lenB):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
