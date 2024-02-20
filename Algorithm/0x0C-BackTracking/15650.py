import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

def sol(start):
    if len(s) == m:
        print(*s)

    for i in range(start, n+1):
        if not visited[i]:
            s.append(i)
            visited[i] = True
            sol(i + 1)
            s.pop()
            visited[i] = False

sol(1)