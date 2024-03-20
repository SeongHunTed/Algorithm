from collections import deque

def processToRoom(array):
    room = []
    for row in array:
        room.append(list(map(str, row)))
    return room
    
def properDistance(room):
    persons = []
    result = True
    for i in range(5):
        for j in range(5):
            if room[i][j] == "P":
                visited = [[False] * (5) for _ in range(5)]
                if bfs(i, j, visited, room) == False:
                    return False
    return True

def bfs(x, y, visited, room):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    
    while q:
        a, b, count = q.popleft()
        
        if count >= 2:
            break
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if room[nx][ny] == "P":
                    return False
                elif room[nx][ny] == "O":
                    q.append((nx, ny, count+1))
                    visited[nx][ny] = True

    return True
    
def solution(places):
    answer = [1] * 5
    for index, place in enumerate(places):
        room = processToRoom(place)
        if not properDistance(room):
            answer[index] = 0
        
    return answer