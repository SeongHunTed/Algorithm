import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

r, c = map(int, input().split())
field = []

for i in range(r):
    field.append(list(input().strip()))

visited = [[False] * c for _ in range(r)]

def dfs(x, y):
    global wolf, sheep
    visited[x][y] = True
        
    if field[x][y] == "v":
        wolf += 1

    if field[x][y] == "o":
        sheep += 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and field[nx][ny] != "#":
            dfs(nx, ny)


sheepTotal = 0
wolfTotal = 0

for i in range(r):
    for j in range(c):
        if field[i][j] != "#" and not visited[i][j]:
            wolf = 0
            sheep = 0
            dfs(i, j)
            if sheep > wolf:
                sheepTotal += sheep
            else:
                wolfTotal += wolf


print(sheepTotal, wolfTotal)