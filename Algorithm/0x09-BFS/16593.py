import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

def bfs():
    while q:
        number, count = q.popleft()
        if number > b:
            continue
        if number == b:
            return count + 1

        q.append((2 * number, count + 1))
        q.append((number * 10 + 1, count + 1))

    return -1

q = deque()
q.append((a, 0))

print(bfs())