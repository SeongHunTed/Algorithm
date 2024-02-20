import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = []
minimumDifference = 2000000001
end = 0

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

for start in range(n):
    while end < n and numbers[end] - numbers[start] < m: end += 1    
    if end == n: break
    minimumDifference = min(minimumDifference, numbers[end]-numbers[start])

print(minimumDifference)