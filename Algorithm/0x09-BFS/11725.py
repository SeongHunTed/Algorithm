import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def dfs(start):
    for node in graph[start]:
        if not visited[node]:
            visited[node] = start
            dfs(node)

def bfs(q):
    while q:
        root = q.popleft()
        for node in graph[root]:
            if not visited[node]:
                visited[node] = root
                q.append(node)


graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    node1, node2 = map(int, input().split(" "))
    graph[node1].append(node2)
    graph[node2].append(node1)

visited[1] = 1
# dfs(1)

q = deque()
q.append(1)
bfs(q)

for i in range(2, n+1):
    print(visited[i])