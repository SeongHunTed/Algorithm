from collections import deque

subin, sis = map(int, input().split())

def findMySister(mover, target):
    second = 0
    visit = [-1] * 100001
    
    q = deque()
    q.append(mover)
    visit[mover] = 0

    while q:
        position = q.popleft()
        if position == target:
            # print(visit[0:100])
            return visit[target]
        
        nx = position * 2
        if 0 <= nx <= 100000 and visit[nx] == -1:
            q.append(nx)
            visit[nx] = visit[position]

        nx = position - 1
        if 0 <= nx <= 100000 and visit[nx] == -1:
            q.append(nx)
            visit[nx] = visit[position] + 1
        
        nx = position + 1
        if 0 <= nx <= 100000 and visit[nx] == -1:
            q.append(nx)
            visit[nx] = visit[position] + 1

        

print(findMySister(subin, sis))