import sys
n, m = map(int, input().split())

x, y, user_side = map(int, input().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

side_move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
count = 1
side_count = 0

while True:
    user_side -= 1
    if user_side < 0:
        user_side = 3
    next_x = x + side_move[user_side][0]
    next_y = y + side_move[user_side][1]

    if world[next_x][next_y] == 1:
        if side_count == 4:
            break
        side_count += 1
        pass
    else:
        world[x][y] = 1
        x = x + side_move[user_side][0]
        y = y + side_move[user_side][1]
        count += 1
        side_count = 0

print(count)
print(world)