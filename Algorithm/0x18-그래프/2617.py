import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
mid = (n+1)/2
result = 0

heavy = [[] for _ in range(n+1)]
light = [[] for _ in range(n+1)]

def dfs(list, start):
    count = 0
    for node in list[start]:
        if not visited[node]:
            visited[node] = True
            count += 1
            count += dfs(list, node)

    return count

for _ in range(m):
    u, v = map(int, input().split())
    heavy[u].append(v)
    light[v].append(u)

for i in range(1, n+1):
    visited = [False] * (n+1)
    if dfs(heavy, i) >= mid:
        result += 1
    if dfs(light, i) >= mid:
        result += 1

print(result)

