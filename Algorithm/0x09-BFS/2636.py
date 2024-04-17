import sys
from collections import deque
input = sys.stdin.readline

# r, c = map(int, input().split())

# cheese = [[0] for _ in range(r+1)]

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# for i in range(1, r+1):
#     cheese[i].extend(list(map(int, input().split())))

# def findHole(i, j):
#     q = deque()
#     q.append((i, j))
#     visited = [[False] * (c+1) for _ in range(r+1)]
#     visited[i][j] = True

#     while q:
#         x, y = q.popleft()

#         if x == 0 or x == r or y == 0 or y == c:
#             for a in range(2, r):
#                 for b in range(2, c):
#                     if visited[a][b]:
#                         cheese[a][b] = -1
#             return

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 1 <= nx <= r and 1 <= ny <= c and not visited[nx][ny]:
#                 if cheese[nx][ny] == 0:
#                     visited[nx][ny] = True
#                     q.append((nx, ny))


# def isThereCheese():
#     count = 0

#     for i in range(2, r):
#         for j in range(2, c):
#             if cheese[i][j] == 1:
#                 count += 1
            
#     return count

# def cheeseKill(i, j):
#     q = deque()
#     q.append((i, j))
#     visited[i][j] = True

#     while q:
#         x, y = q.popleft()

#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]

#             if 1 <= nx <= r and 1 <= ny <= c and not visited[nx][ny]:
#                 if cheese[nx][ny] == -1:
#                     q.append((nx, ny))
#                     visited[nx][ny] = True
#                 elif cheese[nx][ny] == 1:
#                     cheese[nx][ny] = -1
#                     visited[nx][ny] = True
#                 elif cheese[nx][ny] == 0:
#                     cheese[nx][ny] = -1
#                     visited[nx][ny] = True
#                     q.append((nx, ny))


# # 구멍을 뺀 나머지는 -1로 초기화
# for i in range(2, r):
#     for j in range(2, c):
#         if cheese[i][j] == 0:
#             findHole(i, j)

# result = []
# while True:

#     isCheese = isThereCheese()
#     if not isCheese:
#         break
#     else:
#         result.append(isCheese)


#     visited = [[False] * (c+1) for _ in range(r+1)]

#     for i in range(2, r):
#         for j in range(2, c):
#             if cheese[i][j] == -1 and not visited[i][j]:
#                 cheeseKill(i, j)

# print(len(result))
# print(result[-1])

def bfs():
    q = deque()
    q.append((0, 0))
    melt = deque()
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheese[nx][ny] == 0:
                    q.append((nx, ny))
                elif cheese[nx][ny] == 1:
                    melt.append((nx, ny))

    for x, y in melt:
        cheese[x][y] = 0

    return len(melt)

r, c = map(int, input().split())
cheese = []
count = 0
for i in range(r):
    cheese.append(list(map(int, input().split())))
    count += sum(cheese[i])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

time = 1

while True:
    visited = [[0] * c for _ in range(r)]
    meltCount = bfs()
    count -= meltCount
    if count == 0:
        print(time)
        print(meltCount)
        break
    time += 1