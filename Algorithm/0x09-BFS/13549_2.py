import sys
from collections import deque
input = sys.stdin.readline

subin, sister = map(int, input().split())

dx = [0, -1, 1]
visited = [-1] * 100001

def findHer(a, b):
    q = deque()
    visited[a] = 0
    q.append(a)

    while q:
        pos = q.popleft()

        if pos == b:
            return visited[b]
        
        for i in range(3):
            if i == 0:
                nx = pos * 2
                if 0 <= nx <= 100000 and visited[nx] == -1:
                    q.append(nx)
                    visited[nx] = visited[pos]
            else:
                nx = pos + dx[i]
                if 0 <= nx <= 100000 and visited[nx] == -1:
                    q.append(nx)
                    visited[nx] = visited[pos] + 1

print(findHer(subin, sister))