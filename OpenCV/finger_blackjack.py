from cvzone.HandTrackingModule import HandDetector
import cv2
import random
import time
import pygame
import sys
import os
import pygame_menu

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
white = (255, 255, 255)
black = (0, 0, 0)
fps = 30

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
pygame.init()
pygame.display.set_caption("Blackjack")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()

detector = HandDetector(detectionCon=0.8)

fx, fy, l = 0, 0, 0
console = ""
index = 0


class Player(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.score = 0
        self.bonus = 1
        self.images = []

    def add(self):
        self.score = 0
        for image in self.images:
            self.score += values[image[0]]

    def shuffle(self):
        images = os.listdir("cards/")
        image = images[random.randint(0, len(images) - 1)]
        if cards[image[0]] == 0:
            self.shuffle()
        self.images.append(image)
        cards[image[0]] -= 1

    def draw(self, order, image):
        if order:
            path = "cards/{}"
        else:
            path = "functions/{}"
        image = pygame.image.load(path.format(image)).convert_alpha()
        image = pygame.transform.scale(image, (100, 150))
        screen.blit(image, (self.x, self.y))


def audio(name, wait):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    time.sleep(wait)
    pygame.mixer.music.stop()


def finish(message):
    text = font.render(message, True, black)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery - 40
    screen.blit(text, textRect)


def check_win():
    if player.score >= 51 or computer.score >= 51:
        if player.score > 51:
            finish("Bust! Computer won!")
        elif player.score == 51:
            finish("{} won!".format(name.get_value()))
        if computer.score > 51:
            finish("Bust! {} won!".format(name.get_value()))
        elif computer.score == 51:
            finish("Computer won!")
        text = font.render("{} score: {} / Computer score: {}".format(name.get_value(), player.score, computer.score), True, black)
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 30
        screen.blit(text, textRect)
        return True
    return False


def computer_turn(difficulty, order):
    if not termination:
        if not order:
            if difficulty == 1:
                computer.shuffle()
                computer.add()
                order = True
            else:
                expectancy = 0
                for i in range(len(ranks)):
                    expectancy = expectancy + values[ranks[i]] * cards[ranks[i]] / sum(cards.values())
                if computer.score + expectancy <= 21:
                    computer.shuffle()
                    computer.add()
                order = True
        for i in range(3):
            img = pygame.image.load("functions/hit.png").convert_alpha()
            img = pygame.transform.scale(img, (100, 150))
            screen.blit(img, (350 + 6 * i, 230))
        img = pygame.image.load("functions/stay.png").convert_alpha()
        img = pygame.transform.scale(img, (250, 200))
        screen.blit(img, (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 80))
    return order


def show_cards():
    for img in player.images:
        order = True
        player.draw(order, img)
        player.x += 20
    for i in range(len(computer.images)):
        order = False
        computer.draw(order, "hit.png")
        computer.x -= 20


def show_turn(order):
    if order:
        mark = "-{}-".format(name.get_value())
        text = font.render(mark, True, black)
        textRect = text.get_rect()
        textRect.centerx = 108
        textRect.centery = 50
        # text = pygame.transform.scale(text, (150, 50))
        screen.blit(text, textRect)
    else:
        mark = "-Computer-"
        text = font.render(mark, True, black)
        textRect = text.get_rect()
        textRect.centerx = 144
        textRect.centery = 50
        # text = pygame.transform.scale(text, (220, 50))
        screen.blit(text, textRect)


player = Player()
computer = Player()

values = {'a': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 't': 10, 'j': 10,
          'q': 10, 'k': 10}
cards = {'a': 3, '1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3, 't': 3, 'j': 3,
         'q': 3, 'k': 3}
ranks = ('a', '1', '2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k')

player.x = 50
player.y = 400
computer.x = 850
computer.y = 50
termination = False

case = random.randint(0, 1)
if case == 0:
    turn = True
else:
    turn = False

for i in range(2):
    player.shuffle()
    computer.shuffle()

font = pygame.font.SysFont("cambria", 48)

player.add()
computer.add()
selection = [1]

fx, fy, l = 0, 0, 0
console = ""
index = 0


def set_difficulty(_, level):
    selection.append(level)


def start_the_game():
    global turn, termination, fx, fy, l
    while True:
        ret, frame = cap.read()
        hands, frame = detector.findHands(frame)
        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            l, _, _ = detector.findDistance(lmList1[8], lmList1[12], frame)
            fx, fy = lmList1[8][0], lmList1[8][1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if turn:
                if 200 <= fx <= 500 and 200 <= fy <= 400 and l < 40:
                    audio('hit.ogg', 0.7)
                    player.shuffle()
                    player.add()
                    turn = False
                if 505 <= fx <= 684 and 200 <= fy <= 400 and l < 40:
                    audio('stay.ogg', 0.7)
                    turn = False
        pygame.time.delay(10)
        screen.fill([0, 0, 0])
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame.swapaxes(0, 1)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))

        clock.tick(fps)

        termination = check_win()
        show_cards()
        show_turn(turn)
        turn = computer_turn(selection[len(selection) - 1], turn)

        player.x = 50
        computer.x = 850
        pygame.display.update()


menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
name = menu.add.text_input('Name: ', default='Player')
menu.add.selector('Difficulty: ', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
