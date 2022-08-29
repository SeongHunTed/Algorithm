# import sys
# sys.stdin = open('input.txt', 'r')
#
# T = int(input())
# N = 100
# lst = [list(map(int, input().split())) for _ in range(N)]
#
# def ladder(dx, dy):
#     global lst
#     dy -= 1
#     while True:
#         px, py = dx, dy
#         if lst[dy][dx - 1] == 1:
#             dx = dx - 1
#             lst[py][px] = '#'
#             px = dx - 1
#         elif lst[dy][dx + 1] == 1:
#             dx = dx + 1
#             lst[py][px] = '#'
#             px = dx + 1
#         else:
#             dy -= 1
#             lst[py][px] = '#'
#
#         if dy == 0:
#             break
#     return dx
#
#
# y = 99
# x = lst[y].index(2)
#
# print(ladder(x, y))
# print(lst)
#
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
N = 100
lst = [list(map(int, input().split())) for _ in range(N)]

print(lst[99])

def take_ladder(data, start_r, start_c, start):
    pr = start_r
    pc = start_c

    if data[start_r][start_c] == 2:
        print('끝!', start)
        return start

    if 0 <= start_r < N and 0 <= start_c < N and 0 <= start_c - 1 < N and 0 <= start_c + 1 < N and 0 <= start_r + 1 < N:
        if data[start_r][start_c - 1] == 1:
            data[pr][pc] = '#'
            start_c -= 1
            return take_ladder(data, start_r, start_c, start)

        elif data[start_r][start_c + 1] == 1:
            data[pr][pc] = '#'
            start_c += 1
            return take_ladder(data, start_r, start_c, start)

        elif data[start_r + 1][start_c] == 1 or data[start_r + 1][start_c] == 2:
            start_r += 1
            return take_ladder(data, start_r, start_c, start)


start_point = []

for i in range(N):
    if lst[0][i] == 1:
        start_point.append(i)


for s in start_point:
    result = take_ladder(lst, 0, s, s)
    if result is not None:
        print(f'#1 {result}')


