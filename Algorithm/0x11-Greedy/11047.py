import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.reverse()

result = 0

for coin in coins:
    if k == 0: break
    if k // coin > 0:
        result += k // coin
        k = k % coin

print(result)