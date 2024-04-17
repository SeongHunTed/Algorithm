import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

tree = [dict() for _ in range(n+1)]

for _ in range(n-1):
    a, b, weight = map(int, input().split())
    tree[a][b] = weight
    tree[b][a] = weight

def dfs(start, end, count, visited):
    visited[start] = True
    
    if start == end:
        return count
    
    for node in tree[start].keys():
        if not visited[node]:
            result = dfs(node, end, count + tree[start][node], visited)
            if result is not None:
                return result
            visited[node] = False

for _ in range(m):
    visited = [False] * (n+1)
    a, b = map(int, input().split())
    distance = dfs(a, b, 0, visited)
    print(distance)