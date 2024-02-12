import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graphs[v].append(u)

def letsHack(start):
    q = deque()
    q.append(start)
    count = 1

    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        next = q.popleft()
        for i in graphs[next]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                count += 1
    
    return count

result = []
for i in range(1, n+1):
    result.append(letsHack(i))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i + 1, end=' ')