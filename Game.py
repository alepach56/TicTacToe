import pygame
from DrawBoard import drawSquare, drawGrid

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

        pygame.display.flip()
pygame.quit()





