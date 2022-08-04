# import sys
# sys.setrecursionlimit(10000)
# def dfs(x, y):
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if (0 <= nx < n) and (0 <= ny < m):
#             if field[nx][ny] == 1:
#                 field[nx][ny] = -1
#                 dfs(nx, ny)

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(field, x, y):
    queue = [(x, y)]
    field[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=m or ny < 0 or ny >=n:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))


t = int(input())

for i in range(t):
    m, n, cabbage = map(int, input().split())
    cnt = 0
    field = ([[0]*n for _ in range(m)])

    for j in range(cabbage):
        x, y = map(int, input().split())
        field[x][y] = 1

    for i in range(m):
        for j in range(n):
            if field[i][j] > 0:
                # dfs(i, j)
                bfs(field, i, j)
                cnt += 1

    print(cnt)

