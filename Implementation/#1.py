n = int(input())
user_move = input().split()

move = ["L", "R", "U", "D"]
map_ = []

for i in range(n):
    data = []
    for j in range(n):
        data.append((i+1, j+1))
    map_.append(data)

result = [1, 1]


def pathing(x, y):
    for i in range(len(user_move)):
        dir = y[i]
        if dir == 'L':
            if x[1] <= 1:
                pass
            else:
                x[1] -= 1
        elif dir == 'R':
            if x[1] >= n:
                pass
            else:
                x[1] += 1
        elif dir == 'U':
            if x[0] <= 1:
                pass
            else:
                x[0] -= 1
        elif dir == 'D':
            if x[0] >= n:
                pass
            else:
                x[0] += 1

    return x

print()
print(pathing(result, user_move))