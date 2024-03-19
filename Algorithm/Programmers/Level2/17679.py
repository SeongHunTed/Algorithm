def solution(m, n, board):

    gameBoard = []
    # 문자열 분리
    for row in board:
        gameBoard.append(list(map(str, row)))
    
    while True:
        delete = []
        isExist = False
        
        for i in range(m-1):
            for j in range(n-1):
                if gameBoard[i][j] == gameBoard[i+1][j] == gameBoard[i][j+1] == gameBoard[i+1][j+1] and gameBoard[i][j] != 0: 
                    delete.append((i, j)); delete.append((i+1, j))
                    delete.append((i, j+1)); delete.append((i+1, j+1))
                    isExist = True
        
        # 더 이상 제거할 애들이 없음
        if not isExist:
            break
            
        for item in delete:
            x, y = item
            gameBoard[x][y] = 0
        
        # 열을 고정하고 아래로 땡길 예정임
        for i in range(m-1, -1, -1):
            for j in range(n):
                if gameBoard[i][j] == 0:
                    x = i - 1
                    while x >= 0 and gameBoard[x][j] == 0:
                        x -= 1
                    if x < 0:
                        gameBoard[i][j] = 0
                    else:
                        gameBoard[i][j] = gameBoard[x][j]
                        gameBoard[x][j] = 0
        
    answer = 0
    for row in gameBoard:
        answer += row.count(0)

    return answer