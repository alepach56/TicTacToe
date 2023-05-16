import pygame

x_img = pygame.image.load("X.png")
o_img = pygame.image.load("O.png")

x_img = pygame.transform.scale(x_img, (80,80))
o_img = pygame.transform.scale(o_img, (80,80))

winner = None
draw = False
xo = 'x'

from DrawBoard import surface

board = [[None]*3, [None]*3, [None]*3]
posx = 0
posy = 0
row = 0
col = 0



def click(x,y):
    global winner
    global draw
    if (x > 150 and x < 350):
        row = 1
        posx = 200
    elif (x >=350 and x < 550):
        row = 2
        posx = 400
    else:
       row = 3
       posx = 600

    if (y > 150 and y < 350):
        col = 1
        posy = 200
    elif (y >=350 and y < 550):
        col = 2
        posy = 400
    else:
        col = 3
        posy = 600
    if (board[row-1][col-1] != ('x') and board[row-1][col-1] != ('o')):
        board[row-1][col-1] = xo
        addPiece(posx,posy)
        checkWinner()
        if draw:
            message()
        if winner == 'x' or winner == 'o':
            message()
 

def addPiece(posx,posy):
    global xo
    
    if (xo == 'x'):
        surface.blit(x_img, (posx, posy))
        xo = 'o'
        
    else:
        surface.blit(o_img, (posx, posy))
        xo = 'x'
    

def checkWinner():
    global winner
    global draw

    if(all([all(row) for row in board]) and winner is None):
       # pygame.draw.line(surface, (20, 76, 20), (750, 150), (150, 750), 20)
        draw = True

    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pygame.draw.line(surface, (250, 0, 0),
                         (150, (row + 1) * 900 / 3 - 750),
                         (650, (row + 1) *900 / 3 - 150 / 6),
                         20)
            break
 
    # checking for winning columns
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line(surface, (250, 0, 0), ((col + 1) * 900 / 3 - 900 / 6, 0),
                         ((col + 1) * 900 / 3 - 900 / 6, 900), 20)
            break
 
    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
 
        # game won diagonally left to right
        winner = board[0][0]
        pygame.draw.line(surface, (250, 70, 70), (150, 150), (750, 750), 20)
 
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
 
        # game won diagonally right to left
        winner = board[0][2]
        pygame.draw.line(surface, (250, 70, 70), (750, 150), (150, 750), 20)
 
    
        
def message():
    pygame.draw.line(surface, (20, 76, 20), (250, 150), (150, 750), 20)

def updateGame ():
    if winner is None:
        x=1