import math
import itertools

def solution(numbers):
    numbers = makeNumbers(list(numbers))
    answer = fetchPrimeNumberCount(numbers)
    
    return answer

def makeNumbers(numbers):
    nPr = []
    
    for i in range(1, len(numbers)+1):
        nPr += list(itertools.permutations(numbers, i))
    
    results = set()
    for permutation in nPr:
        number = int(''.join([str(char) for char in permutation]))
        results.add(number)
        
    return results

def fetchPrimeNumberCount(numbers):
    if 0 in numbers: numbers.remove(0)
    if 1 in numbers: numbers.remove(1)
    count = 0
    
    for number in numbers:
        isSoSoo = True
        sqrt = int(math.sqrt(number))
        
        for i in range(2, sqrt+1):
            if number % i == 0:
                isSoSoo = False
                break
        
        if isSoSoo: count += 1
    
    return count
        