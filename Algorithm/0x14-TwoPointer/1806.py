import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
end = 0
minmumLength = 100000
subsequenceSum = numbers[0]

for start in range(n):
    while end < n and subsequenceSum < s:
        end += 1
        if end != n: subsequenceSum += numbers[end]
    if end == n: break
    minmumLength = min(minmumLength, end-start+1)
    subsequenceSum -= numbers[start]

if minmumLength == 100000:
    print(0)
else:
    print(minmumLength)