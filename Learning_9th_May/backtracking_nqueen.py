def is_Safe(board, col, row, N):
    #to check down the col (straight line)
    i = col
    while i>=0:
        if board[row][i] == 1:
            return False
        i = i-1

    #to check up the col and row (diagonal)
    i = col 
    j = row
    while i>=0 and j>=0:
        if board[j][i] == 1:
            return False
        i = i-1
        j = j-1

    i=col
    j=row
    #to check down the col and row (diagonal)
    while i>=0 and j<N:
        if board[j][i] == 1:
            return False
        i = i-1
        j = j+1
    
    return True

def N_queen(board, col, N):

    if col >= N:
        return True

    for row in range(N):
        if is_Safe(board,col,row,N):
            board[row][col] = 1  #placing a queen

            if N_queen(board, col+1, N):  #backtracking
                return True
            
            board[row][col] = 0

    return False

N = 4
board = [[0 for i in range(N)] for j in range(N)]
solution = N_queen(board,0,N)
if solution:
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
else: 
    print("solution not found")