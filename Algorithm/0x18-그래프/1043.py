import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
truthAndPeople = list(map(int, input().split()))
number, truthPeople = truthAndPeople[0], [False] * (n+1)
graph = [[] for _ in range(n+1)]
parties = []
visitedParty = [0] * m

if number != 0:
    for man in truthAndPeople[1:]:
        truthPeople[man] = True
else:
    print(m)
    exit(0)

for _ in range(m):
    line = list(map(int, input().split()))
    num, people = line[0], line[1:]
    parties.append(people)

q = deque(truthPeople)
while q:
    x = q.popleft()
    truthPeople[x] = 1
    for i in range(m):
        if x in parties[i]:
            visitedParty[i] = 1
            for y in parties[i]:
                if truthPeople[y] == 0 and y != x:
                    q.append(y)
                    truthPeople[y] = 1

print(visitedParty.count(0))