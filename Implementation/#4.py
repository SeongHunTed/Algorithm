# import sys
# n, m = map(int, input().split())
#
# x, y, user_side = map(int, input().split())
# world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#
# side_move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# count = 1
# side_count = 0
#
# while True:
#     user_side -= 1
#     if user_side < 0:
#         user_side = 3
#     next_x = x + side_move[user_side][0]
#     next_y = y + side_move[user_side][1]
#
#     if world[next_x][next_y] == 1:
#         if side_count == 4:
#             break
#         side_count += 1
#         pass
#     else:
#         world[x][y] = 1
#         x = x + side_move[user_side][0]
#         y = y + side_move[user_side][1]
#         count += 1
#         side_count = 0
#
# print(count)
# print(world)

n, m = map(int, input().split())

d = [[0] * m for i in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)