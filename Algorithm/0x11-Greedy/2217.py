import sys
input = sys.stdin.readline

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()

answer = []
for rope in ropes:
    answer.append(rope * n)
    n -= 1

print(max(answer))