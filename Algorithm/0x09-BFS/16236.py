import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, babySize):
    q = deque()
    q.append((x, y))

    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    visited[x][y] = True

    availableFishLocation = []

    while q:
        a, b, = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]

            if 0 <= na < n and 0 <= nb < n and not visited[na][nb]:
                if jido[na][nb] <= babySize:
                    q.append((na, nb))
                    visited[na][nb] = True
                    dist[na][nb] = dist[a][b] + 1
                    if jido[na][nb] < babySize and jido[na][nb] != 0:
                        availableFishLocation.append((na, nb, dist[na][nb]))
    
    return sorted(availableFishLocation, key=lambda x : (-x[2], -x[0], -x[1]))


n = int(input())
babyX, babyY = 0, 0
babySize = 2
babyStomach = 0
result = 0

# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

jido = []
for _ in range(n):
    jido.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if jido[i][j] == 9:
            babyX, babyY = i, j

while 1:
    shark = bfs(babyX, babyY, babySize)
    
    if len(shark) == 0: break

    nx, ny, dist = shark.pop()
    result += dist
    jido[babyX][babyY], jido[nx][ny] = 0,0

    babyX, babyY = nx, ny
    babyStomach += 1
    if babyStomach == babySize:
        babySize += 1
        babyStomach = 0

print(result)