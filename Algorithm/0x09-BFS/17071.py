import sys
from collections import deque, defaultdict
input = sys.stdin.readline

maxNum = 500001
subin, sis = map(int, input().split())
visited = [-1] * 500001

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def findMySister(mover, target):
    q = deque()
    q.append(mover)
    visited[mover] = 0
    sisterPosition = target

    while q:
        position = q.popleft()

        if position == sisterPosition:
            visited[sisterPosition]

        for nextPosition in (position * 2, position - 1, position + 1):
            if 0 <= nextPosition < maxNum and visited[nextPosition] == -1:
                q.append(nextPosition)
                visited[nextPosition] = visited[position] + 1
                sisterPosition += 1

findMySister(subin, sis)