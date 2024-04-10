def solution(board):
    row = len(board)
    col = len(board[0])
    
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    maxNum = 0
    for row in board:
        maxNum = max(max(row), maxNum)
    
    return maxNum ** 2