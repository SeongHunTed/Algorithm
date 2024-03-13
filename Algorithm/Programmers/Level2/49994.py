def solution(dirs):
    answer = 0
    vector = {'U':[0, 1], 'D':[0, -1], 'R':[1, 0], 'L':[-1, 0]}
    visited = dict()
    for i in range(-5, 6):
        for j in range(-5, 6):
            visited[(i, j)] = set()
    
    x, y = 0, 0
    
    for dir in dirs:
        way = vector[dir]
        nx = x + way[0]
        ny = y + way[1]
        
        if nx < -5 or nx > 5 or ny > 5 or ny < -5:
            continue
        
        if (x, y) in visited[(nx, ny)]:
            x = nx
            y = ny
            pass
        else:
            visited[(x, y)].add((nx, ny))
            visited[(nx, ny)].add((x, y))
            x = nx
            y = ny
            answer += 1
    
    return answer