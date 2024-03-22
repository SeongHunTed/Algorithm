from math import gcd

def solution(w,h):
    answer = 1
    total = w * h
    gcdNum = gcd(w, h)
    
    divideW = w // gcdNum
    divideH = h // gcdNum
    
    impossible = divideW + divideH - 1
    
    return total - impossible * gcdNum