import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
visited = [False] * (n+1)

def sol():
    if len(arr) == m:
        print(*arr)
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            sol()
            arr.pop()
            visited[i] = False

sol()
