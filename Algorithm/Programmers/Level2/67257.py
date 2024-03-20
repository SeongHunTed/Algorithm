from itertools import permutations

def calculate(a, b, operand):
    if operand == "*":
        return a * b
    elif operand == "+":
        return a + b
    else:
        return a - b
    
def solution(expression):
    answer = 0
    operandList = ["*", "+", "-"]
    operands = list(permutations(operandList, 3))
    
    array = []
    numberIndex = 0
    for index, char in enumerate(expression):
        if not char.isdigit():
            array.append(int(expression[numberIndex:index]))
            array.append(char)
            numberIndex = index + 1
    
    array.append(int(expression[numberIndex:]))
    
    for operand in operands:
        first, second, third = operand
        arr = array.copy()
        while True:
            if len(arr) == 1: break
            
            while arr.count(first):
                index = arr.index(first)
                arr = arr[:index-1] + [calculate(arr[index-1], arr[index+1], arr[index])] + arr[index+2:]
            
            while arr.count(second):
                index = arr.index(second)
                arr = arr[:index-1] + [calculate(arr[index-1], arr[index+1], arr[index])] + arr[index+2:]
            
            while arr.count(third):
                index = arr.index(third)
                arr = arr[:index-1] + [calculate(arr[index-1], arr[index+1], arr[index])] + arr[index+2:]
        
        answer = max(answer, abs(arr[0]))
    return answer