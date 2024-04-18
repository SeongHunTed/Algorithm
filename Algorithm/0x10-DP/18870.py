import sys
input = sys.stdin.readline

n = int(input())
positions = list(map(int, input().split()))
numbers = sorted(list(set(positions)))
result = []

for target in positions:
    st, en = 0, len(numbers)
    targetPosition = 0

    while st <= en:
        mid = (st+en) // 2

        if numbers[mid] == target:
            targetPosition = mid
            break
        elif numbers[mid] > target:
            en = mid
        else:
            st = mid

    result.append(targetPosition)

print(' '.join(list(map(str, result))))
