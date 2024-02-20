import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

def sol():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n+1):
        s.append(i)
        sol()
        s.pop()

sol()