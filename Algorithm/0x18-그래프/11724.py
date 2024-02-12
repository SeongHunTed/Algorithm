from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def countByBFS(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def countByDFS(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            countByDFS(i)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        # countByBFS(i)
        countByDFS(i)
        count += 1

print(count)
        