import sys
input = sys.stdin.readline

n = int(input())
meetings = []
time = 0
totalMeetings = 0

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x : (x[1], x[0]))

for meeting in meetings:
    start, end = meeting[0], meeting[1]
    if time <= start:
        time = end
        totalMeetings += 1

print(totalMeetings)