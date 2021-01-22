import pygame


# initialize pygame
pygame.init()
# define size of game container
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
# set a game name to display
pygame.display.set_caption("Hangman Game!")

# load images
images = []
for i in range(7):
    image = pygame.image.load(
        r"C:\Users\Zver\Coding\Hangman Game\images\hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0

# frames per second
FPS = 60
clock = pygame.time.Clock()
run = True

# setup game loop
while run:
    clock.tick(FPS)

    # change window color to white
    window.fill((255, 255, 255))
    pygame.display.update()

    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # getting mouse position
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
