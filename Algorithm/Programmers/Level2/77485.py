def makeBoard(r, c):
    board = [[0] * (c+1) for _ in range(r+1)]
    
    for i in range(1, r+1):
        for j in range(1, c+1):
            board[i][j] = (i-1) * c + j
            
    return board

def rotateResult(startX, startY, endX, endY):
    numbers = [board[startX+1][startY]]
    
    for i in range(startY, endY):
        numbers.append(board[startX][i])
        board[startX][i] = numbers[-2]
    
    for i in range(startX, endX):
        numbers.append(board[i][endY])
        board[i][endY] = numbers[-2]
        
    for i in range(endY, startY, -1):
        numbers.append(board[endX][i])
        board[endX][i] = numbers[-2]
    
    for i in range(endX, startX, -1):
        numbers.append(board[i][startY])
        board[i][startY] = numbers[-2]
        
    return min(numbers)


def solution(rows, columns, queries):
    global board
    board = makeBoard(rows, columns)
    answer = []
    
    for query in queries:
        startX, startY, endX, endY = query
        result = rotateResult(startX, startY, endX, endY)
        answer.append(result)
    
    return answer