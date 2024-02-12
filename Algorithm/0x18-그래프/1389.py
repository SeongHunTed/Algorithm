import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graphs = [[] for _ in range(n+1)]
cabin = [0] * (n+1)
cabinNumber = []

for _ in range(m):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)

def whoIsTheIncca(man):
    q = deque()
    cabin[man] = -1

    for i in graphs[man]:
        q.append((i, 1))
        cabin[i] = 1

    while q:
        friend, count = q.popleft()

        for i in graphs[friend]:
            if cabin[i] == 0:
                cabin[i] = count + 1
                q.append((i, count + 1))

for i in range(1, n+1):
    whoIsTheIncca(i)
    result = 0
    for j in cabin:
        if j != 0 or j != -1:
            result += j
    cabinNumber.append(result)
    cabin = [0] * (n+1)

print(cabinNumber.index(min(cabinNumber)) + 1)
