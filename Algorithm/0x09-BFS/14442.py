from collections import deque
from sys import stdin
input = stdin.readline

r, c, K = map(int, input().split())

visited = [[[0] * (K+1) for _ in range(c)] for _ in range(r)]
miro = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(r):
    miro.append(list(map(int, input().strip())))

def crashAndFindMyWay():
    q = deque()
    q.append((0, 0, K))
    visited[0][0][K] = 1

    while q:
        x, y, k = q.popleft()

        if x == r-1 and y == c-1:
            return visited[x][y][k]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if k > 0 and miro[nx][ny] == 1 and visited[nx][ny][k-1] == 0:
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
                    q.append((nx, ny, k-1))
                elif miro[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    q.append((nx, ny, k))
    return -1

print(crashAndFindMyWay())
