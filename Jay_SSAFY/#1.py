import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
N = 100
lst = [list(map(int, input().split())) for _ in range(N)]

def ladder(dx, dy):
    global lst
    dy -= 1
    while True:
        px, py = dx, dy
        if lst[dy][dx - 1] == 1:
            dx = dx - 1
            lst[py][px] = '#'
            px = dx - 1
        elif lst[dy][dx + 1] == 1:
            dx = dx + 1
            lst[py][px] = '#'
            px = dx + 1
        else:
            dy -= 1
            lst[py][px] = '#'

        if dy == 0:
            break
    return dx


y = 99
x = lst[y].index(2)

print(ladder(x, y))
print(lst)

# import sys
#
# sys.stdin = open('input.txt', 'r')

# 아래 방향 > 좌우 방향 나타날 시 방향 전환 > 아래 방향으로만 이동 > 바닥 도착 시 멈춤


# 2중배열 돌면서 우,하,좌 반복해서 확인
# 만약 우도 갈 수 있고 하도 갈 수 있으면 우로 감, 우로 간뒤 무조건 하 방향으로 전진
# 동시에 좌우 갈 수 있는 경우는 없음

# 답이 표시된 곳은 2 로 표기되어있음
# T = int(input())
# N = 100
# lst = [list(map(int, input().split())) for _ in range(N)]
#
# # 우, 하, 좌
# dr = [0, 1, 0]
# dc = [1, 0, -1]
#
# def take_ladder(lst, start_r, start_c, start, flag):
#     target = 2
#     D = 1
#     new_r = start_r
#     new_c = start_c
#
#     if lst[new_r][new_c] == target:
#         print('끝!', start)
#         return start
#
#
#     if 0 <= new_r < N and 0 <= new_c < N and 0 <= new_c - 1 < N and 0 <= new_c + 1 < N and 0 <= new_r + 1 < N:
#         if lst[new_r][new_c - 1] == 1:
#             lst[new_r][new_c] = '#'
#             new_c -= 1
#             flag = 'left'
#             return take_ladder(lst, new_r, new_c, start, flag)
#
#         elif lst[new_r][new_c + 1] == 1:
#             lst[new_r][new_c] = '#'
#             new_c += 1
#             flag = 'right'
#             return take_ladder(lst, new_r, new_c, start, flag)
#
#         elif lst[new_r + 1][new_c] == 1 or lst[new_r + 1][new_c] == 2:
#             new_r += 1
#             return take_ladder(lst, new_r, new_c, start, flag)
#
#
# start_point = []
#
# for i in range(N):
#     if lst[0][i] == 1:
#         start_point.append(i)
#
# global end_r
# end_r = 0
#
# for start in start_point:
#     if start == 67:
#         flag = 'left'
#         result = take_ladder(lst, 0, start, start, flag)
#         if result is not None:
#             print(f'#1 {result}')


