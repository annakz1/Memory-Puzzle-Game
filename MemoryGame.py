import pygame, sys
from pygame.locals import *
import random

shapes_arrangement = []

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


def startGame():
    for i in range(4):
        if i == 0 or i == 1:
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        x = random.choice(rectangles)
        shapes_arrangement.append(x)
        drawRecShapes(x, color)
        rectangles.remove(x)
    for i in range(4):
        if i == 0 or i == 1:
            color = (255, 255, 0)
        else:
            color = (0, 255, 255)
        x = random.choice(rectangles)
        shapes_arrangement.append(x)
        drawCirShapes(x, color)
        rectangles.remove(x)
    for i in range(4):
        if i == 0 or i == 1:
            color = (255, 0, 255)
        else:
            color = (128, 0, 0)
        x = random.choice(rectangles)
        shapes_arrangement.append(x)
        drawTriShapes(x, color)
        rectangles.remove(x)


def right_choice(first_choice, second_choice):
    x = shape_index(first_choice)
    y = shape_index(second_choice)
    if (x == 0 and y == 1 or x == 1 and y == 0) \
            or (x == 2 and y == 3 or x == 3 and y == 2) \
            or (x == 4 and y == 5 or x == 5 and y == 4) \
            or (x == 6 and y == 7 or x == 7 and y == 6) \
            or (x == 8 and y == 9 or x == 9 and y == 8) \
            or (x == 10 and y == 11 or x == 11 and y == 10) \
            or (x == 12 and y == 13 or x == 13 and y == 12) \
            or (x == 14 and y == 15 or x == 15 and y == 14):
        return True


def shape_index(mouse_position):
    for i in range(12):
        if RectangleObjects[i].collidepoint(mouse_position):
            return shapes_arrangement.index(i + 1)


def rec_number(mouse_position):
    for i in range(12):
        if RectangleObjects[i].collidepoint(mouse_position):
            return i + 1


def hide(mouse_position):
    rectangle_number = rec_number(mouse_position)
    for i in range(12):
        if rectangle_number == i + 1:
            pygame.draw.rect(Window, (255, 255, 255), RectangleObjects[i].inflate(-10, -10))


def show(mouse_position):
    rectangle_number = rec_number(mouse_position)
    shapeindex = shape_index(mouse_position)
    if shapeindex == 0 or shapeindex == 1:
        color = (0, 0, 255)
        drawRecShapes(rectangle_number, color)
    elif shapeindex == 2 or shapeindex == 3:
        color = (0, 255, 0)
        drawRecShapes(rectangle_number, color)
    elif shapeindex == 4 or shapeindex == 5:
        color = (255, 255, 0)
        drawCirShapes(rectangle_number, color)
    elif shapeindex == 6 or shapeindex == 7:
        color = (0, 255, 255)
        drawCirShapes(rectangle_number, color)
    elif shapeindex == 8 or shapeindex == 9:
        color = (255, 0, 255)
        drawTriShapes(rectangle_number, color)
    elif shapeindex == 10 or shapeindex == 11:
        color = (128, 0, 0)
        drawTriShapes(rectangle_number, color)


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
                mouse_position = pygame.mouse.get_pos()
                show(mouse_position)
                pygame.display.update()
                if flag == 0:
                    first_choice = mouse_position
                    if rec_number(first_choice) in true_choices:
                        flag = 0
                    else:
                        flag = 1

                else:
                    second_choice = mouse_position
                    if rec_number(second_choice) in true_choices:
                        flag = 1
                    else:
                        flag = 0
                    if not (rec_number(first_choice) in true_choices) and not (
                            rec_number(second_choice) in true_choices):
                        if right_choice(first_choice, second_choice):
                            true_choices.append(rec_number(first_choice))
                            true_choices.append(rec_number(second_choice))
                        else:
                            pygame.time.wait(1000)
                            hide(first_choice)
                            hide(second_choice)
                            pygame.display.update()


if __name__ == "__main__":
    main()
