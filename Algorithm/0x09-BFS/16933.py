import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

r, c, K = map(int, input().split())
miro = []
visited = [[[0]*(K+1) for _ in range(c)] for _ in range(r)]

for _ in range(r):
    miro.append(list(map(int, input().strip())))

def crashAndFindMyWay():
    q = deque()
    q.append((0, 0, K, True, 1))
    visited[0][0][K] = 1

    while q:
        x, y, k, day, count = q.popleft()

        if x == r-1 and y == c-1:
            # for row in visited:
            #     print(row)
            return visited[x][y][k]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if miro[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = count + 1
                    q.append((nx, ny, k, not day, count +1))
                # 부술 수 있고 낮
                elif k > 0 and day and miro[nx][ny] == 1 and visited[nx][ny][k-1] == 0:
                    visited[nx][ny][k-1] = count + 1
                    q.append((nx, ny, k-1, False, count + 1))
                # 부숴야 되는데 밤
                elif k > 0 and not day and miro[nx][ny] == 1 and visited[nx][ny][k-1] == 0:
                    visited[x][y][k] = count + 1
                    q.append((x, y, k, True, count + 1))

    return -1


print(crashAndFindMyWay())
