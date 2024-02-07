from collections import deque

r, c =  map(int, input().split())
iceMap = [list(map(int, input().split())) for _ in range(r)]
success = False
year = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def meltBfs(i, j, wasLand):
    if wasLand[i][j]:
        return

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < r and 0 <= ny < c and iceMap[nx][ny] > 0:
            wasLand[nx][ny] = True
            iceMap[nx][ny] -= 1

def landBfs(i, j, visited):
    global success

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < r and 0 <= ny < c and iceMap[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    # print(land) 
    return land

    
while not success:
    seaCount = 0
    wasLand = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c) :
            if iceMap[i][j] == 0:
                meltBfs(i, j, wasLand)
                seaCount += 1

    # for row in iceMap:
    #     print(row)
        
    year += 1

    land = 0
    visited = [[False]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if iceMap[i][j] > 0 and not visited[i][j] and land < 2:
                landBfs(i, j, visited)
                land += 1
    if seaCount == r * c and land < 2:
        print(0)
        exit(0)
        
    if land >= 2:
        success = True
        print(year)

