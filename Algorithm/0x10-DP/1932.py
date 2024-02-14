import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
# triangle[1] = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]

if n == 1:
    print(triangle[0][0])
    exit(0)

for i in range(1, n):
    sumValue = []
    for j in range(i + 1):
        if j == 0:
            sumValue.append(triangle[i-1][j] + triangle[i][j])
        elif j == i:
            sumValue.append(triangle[i-1][j-1] + triangle[i][j])
        else:
            sumValue.append(max(triangle[i-1][j-1] + triangle[i][j], triangle[i-1][j] + triangle[i][j]))

    triangle[i] = sumValue

print(max(triangle[n-1]))