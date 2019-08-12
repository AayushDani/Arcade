import numpy

def create():
    board = numpy.zeros((6,7))
    return board

board = create()
end = False
turn = 0
row_count = 6
col_count = 7

def drop(board,row,col,piece):
    board[row][col] = piece
    
def valid_location(board,col):
    return board[5][col] == 0

def next_row(board,col):
    for i in range(row_count):
        if board[i][col] == 0:
            return i

def display(board):
    print(numpy.flip(board,0))

def win_condition(board,piece):
    
    for c in range(col_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(col_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    for c in range(col_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    for c in range(col_count-3):
        for r in range(3,row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            
            
    

display(board)

while not end:
    
    if turn == 0:
        col = int(input('Player 1, which column do you play in?(1 to 7) '))-1

        if valid_location(board,col):
            row = next_row(board,col)
            drop(board,row,col,1)
        display(board)
        if win_condition(board,1):
            print('Player 1 wins')
            end = True
                
    else:
        col = int(input('Player 2, which column do you play in?(1 to 7) '))-1

        
        if valid_location(board,col):
            row = next_row(board,col)
            drop(board,row,col,2)
        display(board)
        if win_condition(board,2):
            print('Player 2 wins')
            end = True

    turn += 1
    turn = turn%2
            
