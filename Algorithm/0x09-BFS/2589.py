import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

jido = [[0] for _ in range(r+1)]

for i in range(1, r+1):
    line = list(input().strip())
    jido[i].extend(line)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * (c+1) for _ in range(r+1)]
    visited[x][y] = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    count = 0

    while q:
        posX, posY = q.popleft()

        for i in range(4):
            nx = posX + dx[i]
            ny = posY + dy[i]

            if 1 <= nx <= r and 1 <= ny <= c and visited[nx][ny] == 0 and jido[nx][ny] == "L":
                visited[nx][ny] = visited[posX][posY] + 1
                q.append((nx, ny))
                count = max(count, visited[nx][ny])

    return count-1

    
result = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        if jido[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)