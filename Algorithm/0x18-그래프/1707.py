import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, visited, graph, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:
            result = dfs(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False
            
    return True



K = int(input())
for _ in range(K):
    v, e = map(int, input().split())
    graphs = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    
    for _ in range(e):
        u, v = map(int, input().split())
        graphs[u].append(v)
        graphs[v].append(u)

    for i in range(1, v+1):
        if visited[i] == 0:
            result = dfs(i, visited, graphs, 1)
            if not result:
                break

    if result:
        print("YES")
    else:
        print("NO")
