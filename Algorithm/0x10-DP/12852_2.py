import sys
input = sys.stdin.readline

n = int(input())
visited = [[0], [1]]

dp = [0] * (n+1)

dp[1] = 0

for i in range(2, n+1):
    root = [i] + visited[i-1]
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        if dp[i] > dp[int(i // 3)] + 1:
            root = [i] + visited[int(i // 3)]
            dp[i] = dp[int(i // 3)] + 1
        
    if i % 2 == 0:
        if dp[i] > dp[int(i // 2)] + 1:
            root = [i] + visited[int(i // 2)]
            dp[i] = dp[int(i // 2)] + 1
    
    visited.append(root)

print(dp[n])
print(' '.join(list(map(str, visited[n]))))