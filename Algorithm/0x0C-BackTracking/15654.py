import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [0] + sorted(list(map(int, input().split())))
s = []
visited = [False] * (n+1)

def sol():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            s.append(numbers[i])
            sol()
            s.pop()
            visited[i] = False

sol()