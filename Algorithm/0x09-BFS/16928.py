import sys
from collections import deque
input = sys.stdin.readline

jido = range(0, 101)
n, m = map(int, input().split())

ladders = {}
for _ in range(n):
    start, end = map(int, input().split())
    ladders[start] = end

snakes = {}
for _ in range(m):
    start, end = map(int, input().split())
    snakes[start] = end

def bfs():
    visited = [False] * 101
    q = deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        now, count = q.popleft()

        if now == 100:
            return count
        
        for i in range(1, 7):
            next = now + i

            if next <= 100 and not visited[next]:
                visited[next] = True
                if next in ladders:
                    visited[ladders[next]] = True
                    q.append((ladders[next], count + 1))
                elif next in snakes:
                    visited[snakes[next]] = True
                    q.append((snakes[next], count + 1))
                else:
                    q.append((next, count + 1))

print(bfs())