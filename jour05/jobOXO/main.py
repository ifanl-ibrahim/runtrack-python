import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TicTacToe1337")

lancement = True
while lancement:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lancement = False

    pygame.display.flip()

pygame.quit()