from collections import deque
n = int(input())

jido = []
for _ in range(n):
    jido.append(list(map(int, input().split())))

# jido = """
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 0 0 0 0 1 1
# 1 0 1 1 0 0 0 0 1 1
# 0 0 1 1 1 0 0 0 0 1
# 0 0 0 1 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# """.split("\n")[1:-1]

# myjido = []

# for row in jido:
#     myjido.append(list(map(int, row.split())))

# jido = myjido

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False]*n for _ in range(n)]

def bfs(i, j):
    global count
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    jido[i][j] = count

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and jido[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                jido[nx][ny] = count

def bfs2(k):
    global result
    q = deque()
    dist = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if jido[i][j] == k:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:

                if jido[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

                if jido[nx][ny] > 0 and jido[nx][ny] != k:
                    result = min(dist[x][y], result)
                    return



count = 1
for i in range(n):
    for j in range(n):
        if jido[i][j] > 0 and not visited[i][j]:
            bfs(i, j)
            count += 1
            
result = 99999999

for i in range(1, count):
    bfs2(i)

print(result)