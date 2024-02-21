def solution(sizes):
    purseSizeX = 0
    purseSizeY = 0
    
    for size in sizes:
        x, y = size[0], size[1]
        if x < y:
            x, y = y, x
        purseSizeX = max(x, purseSizeX)
        purseSizeY = max(y, purseSizeY)
        
    answer = purseSizeX * purseSizeY
    return answer