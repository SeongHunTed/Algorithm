from collections import deque

K = int(input())
c, r = map(int, input().split())
miro = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dhx = [1, 1, -1, -1, 2, 2, -2, -2]
dhy = [2, -2, 2, -2, 1, -1, 1, -1]

for _ in range(r):
    miro.append(list(map(int, input().split())))

def escapeMyMonkey(n):
    q = deque()
    q.append((0, 0, n))
    count = [[[0] * (n+1) for _ in range(c)] for _ in range(r)]

    while q:
        x, y, k = q.popleft()
        if x == r - 1 and y == c - 1:
            return count[x][y][k]
        
        if k > 0:
            for i in range(8):
                nx = x + dhx[i]
                ny = y + dhy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if miro[nx][ny] != 1 and count[nx][ny][k-1] == 0:
                        count[nx][ny][k-1] = count[x][y][k] + 1
                        q.append((nx, ny, k-1))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if miro[nx][ny] != 1 and count[nx][ny][k] == 0:
                    count[nx][ny][k] = count[x][y][k] + 1
                    q.append((nx, ny, k))

    return -1
        
print(escapeMyMonkey(K))