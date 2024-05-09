def is_Safe(board, col, row, N):
    #to check down the col that is straight line
    i = col
    while i>=0:
        if board[row][i] == 1:
            return False
        i = i-1
    
    #to check up the col and row
    i = col, j = row
    while i>=0 and j>=0:
        if board[j][i] == 1:
            return False
        i = i-1
        j = j-1
    
    #to check down the col and row
    while i>=0 and j<N:
        if board[j][i] == 1:
            return False
        i = i-1
        j = j+1
    
    return True


def N_queen(board, col, N):

    if col > N:
        return True

    for row in range(N):
        if is_Safe(board,row,col,N):
            board[row][col] = 1
            N_queen(board, col+1, N)

N = 4
board = [[0 for i in range(N) for j in range(N)]]
print(board)