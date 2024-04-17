import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for item in graph:
    item.sort(reverse=True)

def dfs(start):
    global count
    visited[start] = count

    for node in graph[start]:
        if not visited[node]:
            count += 1
            dfs(node)

visited = [0] * (n+1)
count = 1
dfs(r)

for i in range(1, n+1):
    print(visited[i])
