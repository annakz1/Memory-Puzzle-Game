import pygame, sys
from pygame.locals import *
import random

rectangles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Rectangle1 = Rect(0, 0, 100, 100)
Rectangle2 = Rect(100, 0, 100, 100)
Rectangle3 = Rect(200, 0, 100, 100)
Rectangle4 = Rect(300, 0, 100, 100)
Rectangle5 = Rect(0, 100, 100, 100)
Rectangle6 = Rect(100, 100, 100, 100)
Rectangle7 = Rect(200, 100, 100, 100)
Rectangle8 = Rect(300, 100, 100, 100)
Rectangle9 = Rect(0, 200, 100, 100)
Rectangle10 = Rect(100, 200, 100, 100)
Rectangle11 = Rect(200, 200, 100, 100)
Rectangle12 = Rect(300, 200, 100, 100)

RectangleObjects = (
    Rectangle1, Rectangle2, Rectangle3, Rectangle4, Rectangle5, Rectangle6, Rectangle7, Rectangle8, Rectangle9,
    Rectangle10,
    Rectangle11, Rectangle12)


def drawBackground():
    for i in range(12):
        pygame.draw.rect(Window, (51, 204, 204), RectangleObjects[i], 10)


def drawRecShapes(x, color):
    if x == 1:
        pygame.draw.rect(Window, color, Rect(20, 20, 60, 60))
    elif x == 2:
        pygame.draw.rect(Window, color, Rect(120, 20, 60, 60))
    elif x == 3:
        pygame.draw.rect(Window, color, Rect(220, 20, 60, 60))
    elif x == 4:
        pygame.draw.rect(Window, color, Rect(320, 20, 60, 60))
    elif x == 5:
        pygame.draw.rect(Window, color, Rect(20, 120, 60, 60))
    elif x == 6:
        pygame.draw.rect(Window, color, Rect(120, 120, 60, 60))
    elif x == 7:
        pygame.draw.rect(Window, color, Rect(220, 120, 60, 60))
    elif x == 8:
        pygame.draw.rect(Window, color, Rect(320, 120, 60, 60))
    elif x == 9:
        pygame.draw.rect(Window, color, Rect(20, 220, 60, 60))
    elif x == 10:
        pygame.draw.rect(Window, color, Rect(120, 220, 60, 60))
    elif x == 11:
        pygame.draw.rect(Window, color, Rect(220, 220, 60, 60))
    elif x == 12:
        pygame.draw.rect(Window, color, Rect(320, 220, 60, 60))
    elif x == 13:
        pygame.draw.rect(Window, color, Rect(20, 320, 60, 60))
    elif x == 14:
        pygame.draw.rect(Window, color, Rect(120, 320, 60, 60))
    elif x == 15:
        pygame.draw.rect(Window, color, Rect(220, 320, 60, 60))
    elif x == 16:
        pygame.draw.rect(Window, color, Rect(320, 320, 60, 60))


def drawCirShapes(x, color):
    if x == 1:
        pygame.draw.circle(Window, color, (50, 50), 30)
    elif x == 2:
        pygame.draw.circle(Window, color, (150, 50), 30)
    elif x == 3:
        pygame.draw.circle(Window, color, (250, 50), 30)
    elif x == 4:
        pygame.draw.circle(Window, color, (350, 50), 30)
    elif x == 5:
        pygame.draw.circle(Window, color, (50, 150), 30)
    elif x == 6:
        pygame.draw.circle(Window, color, (150, 150), 30)
    elif x == 7:
        pygame.draw.circle(Window, color, (250, 150), 30)
    elif x == 8:
        pygame.draw.circle(Window, color, (350, 150), 30)
    elif x == 9:
        pygame.draw.circle(Window, color, (50, 250), 30)
    elif x == 10:
        pygame.draw.circle(Window, color, (150, 250), 30)
    elif x == 11:
        pygame.draw.circle(Window, color, (250, 250), 30)
    elif x == 12:
        pygame.draw.circle(Window, color, (350, 250), 30)
    elif x == 13:
        pygame.draw.circle(Window, color, (50, 350), 30)
    elif x == 14:
        pygame.draw.circle(Window, color, (150, 350), 30)
    elif x == 15:
        pygame.draw.circle(Window, color, (250, 350), 30)
    elif x == 16:
        pygame.draw.circle(Window, color, (350, 350), 30)


def drawTriShapes(x, color):
    if x == 1:
        pygame.draw.polygon(Window, color, ((10, 20), (90, 20), (50, 80)))
    elif x == 2:
        pygame.draw.polygon(Window, color, ((110, 20), (190, 20), (150, 80)))
    elif x == 3:
        pygame.draw.polygon(Window, color, ((210, 20), (290, 20), (250, 80)))
    elif x == 4:
        pygame.draw.polygon(Window, color, ((310, 20), (390, 20), (350, 80)))
    elif x == 5:
        pygame.draw.polygon(Window, color, ((10, 120), (90, 120), (50, 180)))
    elif x == 6:
        pygame.draw.polygon(Window, color, ((110, 120), (190, 120), (150, 180)))
    elif x == 7:
        pygame.draw.polygon(Window, color, ((210, 120), (290, 120), (250, 180)))
    elif x == 8:
        pygame.draw.polygon(Window, color, ((310, 120), (390, 120), (350, 180)))
    elif x == 9:
        pygame.draw.polygon(Window, color, ((10, 220), (90, 220), (50, 280)))
    elif x == 10:
        pygame.draw.polygon(Window, color, ((110, 220), (190, 220), (150, 280)))
    elif x == 11:
        pygame.draw.polygon(Window, color, ((210, 220), (290, 220), (250, 280)))
    elif x == 12:
        pygame.draw.polygon(Window, color, ((310, 220), (390, 220), (350, 280)))
    elif x == 13:
        pygame.draw.polygon(Window, color, ((10, 320), (90, 320), (50, 380)))
    elif x == 14:
        pygame.draw.polygon(Window, color, ((110, 320), (190, 320), (150, 380)))
    elif x == 15:
        pygame.draw.polygon(Window, color, ((210, 320), (290, 320), (250, 380)))
    elif x == 16:
        pygame.draw.polygon(Window, color, ((310, 320), (390, 320), (350, 380)))


def drawDiamShapes(x, color):
    if x == 1:
        pygame.draw.polygon(Window, color, ((10, 50), (50, 20), (90, 50), (50, 80)))
    elif x == 2:
        pygame.draw.polygon(Window, color, ((110, 50), (150, 20), (190, 50), (150, 80)))
    elif x == 3:
        pygame.draw.polygon(Window, color, ((210, 50), (250, 20), (290, 50), (250, 80)))
    elif x == 4:
        pygame.draw.polygon(Window, color, ((310, 50), (350, 20), (390, 50), (350, 80)))
    elif x == 5:
        pygame.draw.polygon(Window, color, ((10, 150), (50, 120), (90, 150), (50, 180)))
    elif x == 6:
        pygame.draw.polygon(Window, color, ((110, 150), (150, 120), (190, 150), (150, 180)))
    elif x == 7:
        pygame.draw.polygon(Window, color, ((210, 150), (250, 120), (290, 150), (250, 180)))
    elif x == 8:
        pygame.draw.polygon(Window, color, ((310, 150), (350, 120), (390, 150), (350, 180)))
    elif x == 9:
        pygame.draw.polygon(Window, color, ((10, 250), (50, 220), (90, 250), (50, 280)))
    elif x == 10:
        pygame.draw.polygon(Window, color, ((110, 250), (150, 220), (190, 250), (150, 280)))
    elif x == 11:
        pygame.draw.polygon(Window, color, ((210, 250), (250, 220), (290, 250), (250, 280)))
    elif x == 12:
        pygame.draw.polygon(Window, color, ((310, 250), (350, 220), (390, 250), (350, 280)))
    elif x == 13:
        pygame.draw.polygon(Window, color, ((10, 350), (50, 320), (90, 350), (50, 380)))
    elif x == 14:
        pygame.draw.polygon(Window, color, ((110, 350), (150, 320), (190, 350), (150, 380)))
    elif x == 15:
        pygame.draw.polygon(Window, color, ((210, 350), (250, 320), (290, 350), (250, 380)))
    elif x == 16:
        pygame.draw.polygon(Window, color, ((310, 350), (350, 320), (390, 350), (350, 380)))


def startGame():
    for i in range(4):
        if i == 0 or i == 1:
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        x = random.choice(rectangles)
        drawRecShapes(x, color)
        rectangles.remove(x)
    for i in range(4):
        if i == 0 or i == 1:
            color = (255, 255, 0)
        else:
            color = (0, 255, 255)
        x = random.choice(rectangles)
        drawCirShapes(x, color)
        rectangles.remove(x)
    for i in range(4):
        if i == 0 or i == 1:
            color = (255, 0, 255)
        else:
            color = (128, 0, 0)
        x = random.choice(rectangles)
        drawTriShapes(x, color)
        rectangles.remove(x)
    # for i in range(4):
    #     if i == 0 or i == 1:
    #         color = (128, 128, 0)
    #     else:
    #         color = (128, 0, 128)
    #     x = random.choice(rectangles)
    #     drawDiamShapes(x, color)
    #     rectangles.remove(x)


def main():
    pygame.init()
    global Window
    Window = pygame.display.set_mode((410, 310))
    Window.fill((255, 255, 255))
    pygame.display.set_caption('Memory Game')

    drawBackground()
    startGame()

    # pygame.draw.circle(Window, (255, 255, 0), (50, 50), 30)
    # pygame.draw.polygon(Window, (255, 0, 255), ((110, 20), (190, 20), (150, 80)))
    # pygame.draw.polygon(Window, (0, 255, 0), ((210, 50), (250, 20), (290, 50), (250, 80)))
    # drawRecShapes(11, (0, 0, 0))
    pygame.display.update()
    pygame.time.wait(3000)
    Window.fill((255, 255, 255))
    drawBackground()
    pygame.display.update()
    flag = 0
    true_choices = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mouse_position = pygame.mpuse.get_pos()
                show(mouse_position)
                pygame.display.update()
                if flag == 0:
                    first_choice = mouse_position
                    if recNumber(first_choice) in true_choices:
                        flag = 0
                    else:
                        flag = 1

                else:
                    second_choice = mouse_position
                    if recNumber(second_choice) in true_choices:
                        flag = 1
                    else:
                        flag = 0
                    if not (recNumber(first_choice) in true_choices) and not (recNumber(second_choice) in true_choices):
                        if rightchoice(first_choice, second_choice):
                            true_choices.append(recNumber(first_choice))
                            true_choices.append(recNumber(second_choice))
                        else:
                            pygame.time.wait(1000)
                            hide(first_choice)
                            hode(second_choice)
                            pygame.display.update()

if __name__ == "__main__":
    main()
