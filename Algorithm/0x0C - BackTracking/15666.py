import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [0] + sorted(list(set(map(int, input().split()))))
s = []
def sol(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start, len(numbers)):
        s.append(numbers[i])
        sol(i)
        s.pop()

sol(1)