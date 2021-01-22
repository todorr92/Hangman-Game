import pygame
import math
import random
from words import words


# initialize pygame
pygame.init()
# define size of game container
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
# set a game name to display
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
# ASCII charachters
A = 65
for i in range(26):
    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = starty + (i // 13 * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images
images = []
for i in range(7):
    image = pygame.image.load(
        r"C:\Users\Zver\Coding\Hangman Game\images\hangman" + str(i) + ".png")
    images.append(image)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# game variables
hangman_status = 0
word = random.choice(words).upper()
guessed = []

# setup game loop
# frames per second
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    # change window color to white
    window.fill(WHITE)
    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    window.blit(text, (400, 200))

    # draw buttons: 3 is pixels
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width() /
                               2, y - text.get_width() / 2))

    # draw images
    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() /
                       2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def play_again(message):
    window.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() /
                       2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


while run:
    clock.tick(FPS)

    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # getting mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt(
                        (x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                    if distance < RADIUS:
                        # visible
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You WON!")
        play_again("Play Again?")
        break

    if hangman_status == 6:
        display_message("You LOST!")
        play_again("Play Again?")
        break
