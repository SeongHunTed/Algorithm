import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()
maxWeight = 0

for i in range(0, n):
    # 최소 기준 무게
    targetWeight = ropes[i]
    maxWeight = max(targetWeight * (n - i), maxWeight)

print(maxWeight)
