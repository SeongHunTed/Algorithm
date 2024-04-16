import sys
from collections import deque
input = sys.stdin.readline

testCase = int(input())

def isPrimeNumber(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def bfs(start, target):
    q = deque()
    q.append((start, 0))
    visited[start] = 1

    while q:
        num, count = q.popleft()

        if num == target:
            return count

        for index in range(4):
            for i in range(10):
                nextNumber = list(str(num))
                nextNumber[index] = str(i)
                nextNumber = int(''.join(nextNumber))

                if 1000 <= nextNumber <= 9999 and not visited[nextNumber] and prime[nextNumber]:
                    q.append((nextNumber, count + 1))
                    visited[nextNumber] = 1

    return -1

prime = [False]
for i in range(1, 10000):
    prime.append(isPrimeNumber(i))

for _ in range(testCase):
    visited = [0] * 10000
    a, b = map(int, input().split())
    print(bfs(a, b))