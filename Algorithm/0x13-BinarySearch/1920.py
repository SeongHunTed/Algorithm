import sys
input = sys.stdin.readline

n = int(input())
numbers1 = sorted(list(map(int, input().split())))

m = int(input())
numbers2 = list(map(int, input().split()))

def binarySearch(num, st, en):
    while st <= en:
        mid = (st+en) // 2
        
        if num == numbers1[mid]:
            return 1
        
        if num > numbers1[mid]:
            st = mid + 1
        else:
            en = mid - 1
    
    return 0

for num in numbers2:
    st = 0
    en = n - 1  
    print(binarySearch(num, st, en))
