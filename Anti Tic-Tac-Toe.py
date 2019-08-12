print('     *-*-*-RULES-*-*-*      ')
print()
print('Introducing NEW ANTI TIC-TAC-TOE -(note the keyword *ANTI*)-')
print('Now play NOT to WIN but to LOSE.')
print('The rules are simple:)')
print('All you need to do is select a spot from the given number grid.')
print('The grid is numbered from 0-8, from which you can choose a spot- by selecting a number.')
print('You will be play against the computer and the first one to get 3 in a row LOSES.')
print('And you  are x & get to play first, whereas the computer is o.')
print()
      
import random

#The Game board
board = [0,1,2,
         3,4,5,
         6,7,8]

def show():
    print( board[0],'|',board[1],'|',board[2])
    print('---------')
    print( board[3],'|',board[4],'|',board[5])
    print('---------')
    print( board[6],'|',board[7],'|',board[8])


def checkline(char,spot1,spot2,spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3]==char:
        return(True)

def checkall(char):
    if checkline(char, 0, 1, 2):
        return(True)
    if checkline(char, 3, 4, 5):
        return(True)
    if checkline(char, 6, 7, 8):
        return(True)
    if checkline(char, 0, 3, 6):
        return(True)
    if checkline(char, 1, 4, 7):
        return(True)
    if checkline(char, 2, 5, 8):
        return(True)
    if checkline(char, 2, 4, 6):
        return(True)
    if checkline(char, 0, 4, 8):
        return(True)

def resetBoard(char) :
    # declaring the Game board variable as global before resetting the board
    global board 
    print() # print newline before the board display
    show() # shows the board before resetting it
    board = [0, 1, 2,
             3, 4, 5,
             6, 7, 8]
    if char == 'x' :
        print()
        print (':( Computer Won :(')
    elif char == 'o' :
        print()
        print (':) You Won :)')
    else :
        print()
        print ('!!! Draw !!!')
    print()
    print ('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print ('       :) New Game Board :)         ')
    print ('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    
    
num = 0 # global varibale to track the number of times user has drawn (Max 5)      
while True:
        # Before starting the new game, if previous game resulted
        # in (Won, Lost, Draw)
        if checkall('x') == True :
            num = 0
            resetBoard('x')
            continue
        if checkall('o') == True :
            num = 0
            resetBoard('o')
            continue
        # Declare as Draw as 5th iteration of the user1 is already done
        # and no one Won:(
        if num == 5 : 
            num = 0
            resetBoard('')
            continue

        if num == 0 :
            # to take inputs from the user to continue or quit the Game
            Play = (input('Do you Wanna Play, (Y/N) '))
            if Play == 'Y' or Play == 'y':
                show() # to show the Game board at the start of the game
            elif Play == 'N' or Play == 'n':
                break
            else :
                continue
        
        s = int(input('Select your spot : '))
        if s > 8 or s < 0:
            print ('Invalid input :(')
            continue

        num +=1 # increment the number of moves from the user
        if board[s]!= 'x' and board[s]!= 'o':
            board[s] = 'x' # puts the user1 input as 'x' on the place with index's'
            if checkall('x') == True:
                num = 0
                resetBoard('x')
                continue
            if num < 5 :
                while True:
                    random.seed() #Generates a random number
                    opponent = random.randint(0,8)

                    if board[opponent]!= 'x' and board[opponent]!= 'o':
                        board[opponent] = 'o'
                        if checkall('o') == True:
                            num = 0
                            resetBoard('o')
                        break
        else:
            print('This spot is already taken') # error from the user
            # It was incremented earlier now decrement it to keep it logical
            num -= 1 
        if num != 0 and num < 5:
            # show the board after every move played from computer
            # for all except last move
            show() 



