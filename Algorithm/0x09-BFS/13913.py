from collections import deque

subin, sis = map(int, input().split())
root = [0] * 100001
visit = [-1] * 100001

def path(target):
    wholePath = []
    temp = target
    for _ in range(visit[target] + 1):
        wholePath.append(temp)
        temp = root[temp]
    print(' '.join(map(str, wholePath[::-1])))

def findMySister(mover, target):
    q = deque()
    q.append(mover)
    visit[mover] = 0

    while q:
        position= q.popleft()
        if position == target:
            print(visit[target])
            path(position)
            return
        
        for nextPosition in (position * 2, position - 1, position + 1):
            if 0 <= nextPosition <= 100000 and visit[nextPosition] == -1:
                q.append(nextPosition)
                visit[nextPosition] = visit[position] + 1
                root[nextPosition] = position

findMySister(subin, sis)