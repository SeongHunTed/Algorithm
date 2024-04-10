from itertools import permutations
import copy

def splitExpression(expression):
    numberOperands = []
    
    number = ''
    for char in expression:
        if char.isdigit():
            number += char
        else:
            numberOperands.append(int(number))
            number = ''
            numberOperands.append(char)
    numberOperands.append(int(number))
            
    return numberOperands

def calculate(a, b, operand):
    if operand == "*":
        return a * b
    elif operand == "+":
        return a + b
    else:
        return a - b

def solution(expression):
    operands = ['*', '+', '-']
    results = []
    
    numberOperands = splitExpression(expression)
    candidates = permutations(operands, 3)
    
    for candidate in candidates:
        sequence = copy.deepcopy(numberOperands)

        for operands in candidate:
            
            for operand in operands:
                for _ in range(sequence.count(operand)):
                    index = sequence.index(operand)
                    sequence[index-1:index+2] = [calculate(sequence[index-1], sequence[index+1], operand)]
                    
        results.append(abs(sequence[0]))
            
    return max(results)
    