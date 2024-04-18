import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x : (x[1], x[0]))

did = []
now = 0
for meeting in meetings:
    start, end = meeting
    if start >= now:
        did.append(meeting)
        now = end

print(len(did))
