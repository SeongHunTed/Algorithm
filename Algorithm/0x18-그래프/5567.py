import sys
from collections import deque

input = sys.stdin.readline

numberOfFriends = int(input())
m = int(input())
graph = [[] for _ in range(numberOfFriends + 1)]
friends = [False] * (numberOfFriends + 1)
들러리수 = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def inviteMyFriendsAndOthers():
    global 들러리수
    q = deque()
    friends[1] = True
    for i in graph[1]:
        q.append(i)
        friends[i] = True
        들러리수 += 1
    
    while q:
        friend = q.popleft()

        for i in graph[friend]:
            if not friends[i]:
                friends[i] = True
                들러리수 += 1

inviteMyFriendsAndOthers()
print(들러리수)