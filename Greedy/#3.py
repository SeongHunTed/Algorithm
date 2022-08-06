import sys

n, m = map(int, sys.stdin.readline().split())

card = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

minNum = 0

for i in range(n):
    if minNum < min(card[i]):
        minNum = min(card[i])

print(minNum)