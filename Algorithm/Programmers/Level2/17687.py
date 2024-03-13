from collections import deque

def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ''
    count = 0
    q = deque()
    number = 0
    
    while len(answer) < t:
        count += 1
        turn = count % m
        if turn == 0: turn = m
        if len(q) == 0:
            result = list(convert_notation(number, n))
            number += 1
            for r in result:
                q.append(r)

        target = q.popleft()
        if turn == p:
            answer += str(target)
        
    return answer