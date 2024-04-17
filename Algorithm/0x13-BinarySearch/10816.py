import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))

m = int(input())
numbers = list(map(int, input().split()))

def lower(array, target):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def upper(array, target):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2

        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left

result = []
for num in numbers:
    front = lower(cards, num)
    back = upper(cards, num)
    result.append(back - front)


print(' '.join(list(map(str, result))))