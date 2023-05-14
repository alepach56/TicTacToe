import pygame
from DrawBoard import drawSquare, drawGrid
from Pieces import click

# Constants
pygame.init()
drawSquare()
drawGrid()

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if (x > 150 and x < 750) and (y > 150 and y < 750):
                click(x,y)

        pygame.display.update()
pygame.quit()





