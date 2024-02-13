import sys
input = sys.stdin.readline

testCase = int(input())
zero = [0] * 41
one = [0] * 41

zero[0] = 1
zero[1] = 0
zero[2] = 1

one[0] = 0
one[1] = 1
one[2] = 1

def fib(n):
    global zero, one
    if n >= 3:
        for i in range(3, n+1):
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
    
    print(zero[n], one[n])

for _ in range(testCase):
    n = int(input())
    fib(n)