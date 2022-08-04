N = int(input())
roomState = []

for i in range(0, N):
    roomState.append(list(map(str, input())))
    roomState[i].append('X')
roomState.append(['X' for _ in range(N+1)])

res = [0, 0]


for i in range(0, N+1):
    row_count = 0
    col_count = 0
    for j in range(0, N+1):
        if roomState[i][j] == '.':
            row_count += 1
        elif roomState[i][j] == 'X':
            if row_count < 2:
                row_count = 0
            else:
                res[0] += 1

        if roomState[j][i] == '.':
            col_count += 1
        elif roomState[j][i] == 'X':
            if col_count < 2:
                col_count
            else:
                res[1] += 1

print("{} {}".format(res[0], res[1]))
