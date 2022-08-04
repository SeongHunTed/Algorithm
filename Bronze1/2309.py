short = []
a, b = 0, 0
for _ in range(9):
    short.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        if sum(short) - (short[i] + short[j]) == 100:
            a = short[i]
            b = short[j]
            break

short.remove(a)
short.remove(b)

print('\n'.join(map(str, sorted(short))))