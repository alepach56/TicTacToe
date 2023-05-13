import pygame


WIDTH = 900
HEIGHT = 900
ROWS = 3
COLS = 3
WHITE = (0, 0, 0)

surface = pygame.display.set_mode((900,900))

def drawSquare():
    squareSize = 500
    
    color = (250,250,250)
    pygame.draw.rect(surface, color, pygame.Rect(150,150,600,600))
    



def drawGrid():
    blockSize = 200
    for x in range(150, 750, blockSize):
        for y in range(150, 750, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, WHITE, rect, 10)

    pygame.draw.rect(surface, (200,200,200), pygame.Rect(150, 150, 600, 600),  5)
    