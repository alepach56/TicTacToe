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
        draw = True

    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pygame.draw.line(surface, (250, 0, 0), 
                             (30 + (row + 1) * 200, 175),
                             (30 + (row + 1) * 200, 725), 
                            17)
            break
 
    # checking for winning columns
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line(surface, (250, 0, 0),
                         (175, 30 + (col + 1) * 200),
                         (725, 30 + (col + 1) * 200),
                         17)
            break
 
    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
 
        # game won diagonally left to right
        winner = board[0][0]
        pygame.draw.line(surface, (250, 0, 0), (175, 175), (725, 725), 17)
 
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
 
        # game won diagonally right to left
        winner = board[0][2]
        pygame.draw.line(surface, (250, 0, 0), (725, 175), (175, 715), 17)
 
    
        
def message():
    message = ""
    if winner:
        if winner == "x":
            message = "Winner is x!"
        else:
            message = "Winner is o!"
    else:
        message = "The game ends in a draw."

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(message, True, (250,0,0), (0,0,0))
    textRect = pygame.draw.rect(surface, (0,0,0), pygame.Rect(350,800,450,800))
    surface.blit(text, textRect)
    
