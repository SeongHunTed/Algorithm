def solution(arr):
    result = 1
    
    for i in arr:
        result = choisogongbasoo(result, i)
        
    return result
    
def gcd(x, y):
    while y:
        x, y = y, x%y
        
    return x

def choisogongbasoo(x, y):
    return x * y // gcd(x, y)