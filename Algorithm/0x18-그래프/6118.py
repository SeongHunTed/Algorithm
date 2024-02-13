import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graphs = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)

def hide():
    q = deque()
    q.append((1, 1))

    visited[1] = 1

    while q:
        next, count = q.popleft()
        for i in graphs[next]:
            if visited[i] == 0:
                visited[i] = count + 1
                q.append((i, count + 1))

hide()
maxNum = max(visited)
number = visited.index(maxNum)
dist = maxNum - 1
count = visited.count(maxNum)

print(number, dist, count)

