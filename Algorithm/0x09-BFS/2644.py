import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split(" "))

relations = int(input())
chon = [[] for _ in range(n+1)]

for i in range(relations):
    x, y = map(int, input().split(" "))
    chon[x].append(y)
    chon[y].append(x)

def dfs(v, count):
    if v == end:
        return count
    
    for node in chon[v]:
        if not visited[node]:
            visited[node] = True
            result = dfs(node, count+1)
            if result != -1:
                return result

    return -1

visited = [False] * (n+1)
visited[start] = 1
result = dfs(start, 0)
print(result)