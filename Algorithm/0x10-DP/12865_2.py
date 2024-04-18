import sys
input = sys.stdin.readline

n, k = map(int, input().split())

stuffs = []

for _ in range(n):
    v, w = map(int, input().split())
    stuffs.append([v, w])

dp = [[0] * (k+1) for _ in range(n)]
