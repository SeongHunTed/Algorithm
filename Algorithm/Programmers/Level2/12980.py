def solution(n):
    
    batteryWaste = 0
    number = n
    
    if n == 1: return 1
    
    while True:
        if number % 2 != 0:
            number -= 1
            batteryWaste += 1
            continue
        else:
            number = number / 2
            
        if number == 1:
            break
    
    return batteryWaste + 1
            