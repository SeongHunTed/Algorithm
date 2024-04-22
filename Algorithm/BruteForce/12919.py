import sys

s = list(input())
t = list(input())

def process(t):
    if t == s:
        print(1)
        exit()
    if len(t) == 0:
        return 0
    
    if t[-1] == 'A':
        process(t[:-1])

    if t[0] == 'B':
        process(t[1:][::-1])
    
    
process(t)
print(0)