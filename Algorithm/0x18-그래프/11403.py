import sys

input = sys.stdin.readline

n = int(input())
graphs = []
visited = [False] * n

for _ in range(n):
    graphs.append(list(map(int, input().split())))

def canIGo(a):
    for i in range(n):
        if graphs[a][i] == 1 and not visited[i]:
            visited[i] = True
            canIGo(i)

for i in range(n):
    canIGo(i)
    for j in range(n):
        if visited[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [False] * n