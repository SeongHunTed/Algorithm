# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [[] for _ in range(n+1)]

# for a in range(1, n+1):
#     b = int(input())
#     graph[b].append(a)

# visited = [False] * (n+1)
# result = []

# def dfs(node, route):
#     route.add(node)
#     visited[node] = True

#     for i in graph[node]:
#         if i not in route:
#             dfs(i, route.copy())