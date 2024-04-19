import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, (input().split())))

x, y = 0, 0
st = 0
en = n-1
total = 1e10
candidates = {}

while st < en:
    sumation = liquid[st] + liquid[en]

    if abs(sumation) < total:
        total = abs(sumation)
        x = liquid[st]
        y = liquid[en]

    if sumation <= 0:
        st += 1
    elif sumation > 0:
        en -= 1

    
print(x, y)