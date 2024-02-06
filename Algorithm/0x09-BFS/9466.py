import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

testCase = int(input())

def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    num = pick[v]

    if visited[num]:
        if num in cycle: # 4 7 6
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

for _ in range(testCase):
    number = int(input())
    pick = [0] + list(map(int, input().split()))
    visited = [True] + [False]*number
    result = []

    for i in range(1, number + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(number - len(result))
