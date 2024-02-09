import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
switchInfo = defaultdict(list)
for _ in range(m):
    sx, sy, tx, ty = map(int, input().split())
    switchInfo[(sx-1, sy-1)].append((tx-1, ty-1))

def imSoAfraidOfDark():
    result = 1
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    lights = [[0] * n for _ in range(n)]
    lights[0][0] = 1
    q = deque()
    q.append([0, 0])

    while q:
        x, y = q.popleft()
        for tx, ty in switchInfo[(x, y)]:
            if not lights[tx][ty]:
                lights[tx][ty] = 1
                result += 1

                for i in range(4):
                    nx = tx + dx[i]
                    ny = ty + dy[i]

                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]:
                        q.append((nx, ny))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and lights[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

    return result

print(imSoAfraidOfDark())