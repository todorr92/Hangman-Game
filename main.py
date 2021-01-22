import pygame
import os

# initialize pygame
pygame.init()
# define size of game container
WIDTH, HEIGHT = 800, 500
pygame.display.set_mode((WIDTH, HEIGHT))
# set a game name to display
pygame.display.set_caption("Hangman Game!")
# frames per second
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # getting mouse position
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
