import sys
from collections import deque
input = sys.stdin.readline

r, c, number = map(int, input().split())
players = [ str(i) for i in range(1, number)]
playerArea = list(map(int, input().split()))
visited = [[False] * c for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

miro = []
for _ in range(r):
    miro.append(list(map(str, input().strip())))

def fightForTheTerritory():
    end = False
    index = 0

    while not end:
        q = deque()
        for i in range(r):
            for j in range(c):
                if miro[i][j] == players[index] and not visited[i][j]:
                    q.append((i, j, miro[i][j]))
                    visited[i][j] = True

        x, y, player = q.popleft()

        for i in range(1, playerArea[index]):
            for j in range(4):
                nx = x + dx[j] * i
                ny = y + dy[j] * i

                if 0 <= nx < r and 0 <= ny < r:
                    if miro[i][j] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        miro[nx][ny] == player[index]

        index = (index + 1) % len(players)

        if index == 3:
            end = True
        
        for row in miro:
            print(row)
        print()

fightForTheTerritory()


