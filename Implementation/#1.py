# n = int(input())
# user_move = input().split()
#
# move = ["L", "R", "U", "D"]
# map_ = []
#
# for i in range(n):
#     data = []
#     for j in range(n):
#         data.append((i+1, j+1))
#     map_.append(data)
#
# result = [1, 1]
#
#
# def pathing(x, y):
#     for i in range(len(user_move)):
#         dir = y[i]
#         if dir == 'L':
#             if x[1] <= 1:
#                 pass
#             else:
#                 x[1] -= 1
#         elif dir == 'R':
#             if x[1] >= n:
#                 pass
#             else:
#                 x[1] += 1
#         elif dir == 'U':
#             if x[0] <= 1:
#                 pass
#             else:
#                 x[0] -= 1
#         elif dir == 'D':
#             if x[0] >= n:
#                 pass
#             else:
#                 x[0] += 1
#
#     return x
#
# print(pathing(result, user_move))

# 정답풀이

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)