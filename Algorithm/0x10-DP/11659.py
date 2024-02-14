import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
problems = [list(map(int, input().split())) for _ in range(m)]

for i in range(1, n+1):
    numbers[i] = numbers[i-1] + numbers[i]

for problem in problems:
    i, j = problem[0], problem[1]
    print(numbers[j] - numbers[i-1])