import sys
from collections import deque
input = sys.stdin.readline

people = int(input())
graphs = [[] for _ in range(people + 1)]
far = [-1] * (people + 1)
result = []

while 1:
    u, v = map(int, input().split())
    if u == -1: break
    graphs[u].append(v)
    graphs[v].append(u)

def scoring(me):
    q = deque()
    far[me] = 0

    for i in graphs[me]:
        far[i] = 1
        q.append((i, 2))

    while q:
        friend, score = q.popleft()

        for i in graphs[friend]:
            if far[i] == -1 or far[i] > score:
                far[i] = score
                q.append((i, score + 1))

for i in range(1, people+1):
    scoring(i)
    result.append(far)
    far = [-1] * (people + 1)

finalResult = []
for index, array in enumerate(result):
    finalResult.append((max(array), index + 1))

realFinal = sorted(finalResult, key= lambda x : x[0])
maxScore = realFinal[0][0]

hubo = []
for element in realFinal:
    if element[0] == maxScore:
        hubo.append(element[1])

print(maxScore, len(hubo))
print(*hubo)

    
# 1 = 2
# 2 = 3, 4
# 3 = 4
# 4 = 5
# 5 = 3

# [-1, 0, 1, 2, 2, 3] 1
# [-1, 1, 0, 1, 1, 2] 2
# [-1, 2, 1, 0, 1, 1] 3
# [-1, 2, 1, 1, 0, 1] 4
# [-1, 3, 2, 1, 1, 0] 5
    
# 1 -> 2, 2 -> 3, 2 -> 4, 2 -> 4 -> 5 == 3점
# 2 -> 3, 4, 1, 4-> 5 == 2점
# 3 -> 2, 4, 5, 2 -> 1 == 2점
# 4 -> 5, 2, 3, 2 -> 1 == 2점
# 5 -> 3, 4, 3 -> 2, 3 -> 2 -> 1 == 3점


# 2점 3명
# 2, 3, 4