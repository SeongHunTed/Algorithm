import sys

n = int(input())
data = []
new_data = []

for i in range(n):
    data.append(int(input()))

def mySort(x):
    for i in range(n-1):
        for j in range(n-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

print(mySort(data))

