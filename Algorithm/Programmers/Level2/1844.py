from collections import deque

def findExit(maps):
    r = len(maps)
    c = len(maps[0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited = [[0] * c for _ in range(r)]
    
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        if x == r-1 and y == c-1:
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                
    return -1

def solution(maps):
    answer = findExit(maps)
    return answer