import sys
from collections import deque
input = sys.stdin.readline

n ,l, r = map(int, input().split())
jido = [[0] for _ in range(n+1)]

for i in range(1, n+1):
    nations = list(map(int, input().split()))
    jido[i].extend(nations)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    nations = set()
    nations.add((x, y))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        posX, posY = q.popleft()

        for i in range(4):
            nx = posX + dx[i]
            ny = posY + dy[i]

            if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
                if l <= abs(jido[nx][ny] - jido[posX][posY]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    nations.add((nx, ny))

    return nations

count = 0

while True:
    visited = [[False] * (n+1) for _ in range(n+1)]
    flag = True
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not visited[i][j]:
                nations = bfs(i, j)
                if len(nations) > 1:
                    flag = False
                    total = sum(jido[x][y] for x, y in nations) // len(nations)
                    for x, y in nations:
                        jido[x][y] = total

    if flag: break
    count += 1

print(count)


