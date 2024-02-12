import sys
from collections import deque
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [ [] for _ in range(n+1)]

dfsroot = []
bfsroot = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visited[start] = True
    dfsroot.append(start)
    for i in sorted(graph[start]):
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = True
    bfsroot.append(start)

    while q:
        v = q.popleft()
        for i in sorted(graph[v]):
            if not visited[i]:
                q.append(i)
                visited[i] = True
                bfsroot.append(i)


visited = [False] * (n+1)
dfs(start)

visited = [False] * (n+1)
bfs(start)

print(*dfsroot, sep = ' ')
print(*bfsroot, sep = ' ')