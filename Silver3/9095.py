n = int(input())

count = 0
def recursive(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        return recursive(a-1) + recursive(a-2) + recursive(a-3)
x = []
for i in range(n):
    x.append(int(input()))

for i in range(n):
    print(recursive(x[i]))


