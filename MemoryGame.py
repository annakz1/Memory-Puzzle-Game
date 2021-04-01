import pygame, sys
from pygame.locals import *
import random

IMAGES_PATH_ROOT = 'data/results'
IMG_PAIR_0_1 = IMAGES_PATH_ROOT + '/pair0_1.jpeg'
IMG_PAIR_0_2 = IMAGES_PATH_ROOT + '/pair0_2.jpeg'
IMG_PAIR_1_1 = IMAGES_PATH_ROOT + '/pair1_1.jpeg'
IMG_PAIR_1_2 = IMAGES_PATH_ROOT + '/pair1_2.jpeg'
IMG_PAIR_2_1 = IMAGES_PATH_ROOT + '/pair2_1.jpeg'
IMG_PAIR_2_2 = IMAGES_PATH_ROOT + '/pair2_2.jpeg'
IMG_PAIR_3_1 = IMAGES_PATH_ROOT + '/pair3_1.jpeg'
IMG_PAIR_3_2 = IMAGES_PATH_ROOT + '/pair3_2.jpeg'
IMG_PAIR_4_1 = IMAGES_PATH_ROOT + '/pair4_1.jpeg'
IMG_PAIR_4_2 = IMAGES_PATH_ROOT + '/pair4_2.jpeg'
IMG_PAIR_5_1 = IMAGES_PATH_ROOT + '/pair5_1.jpeg'
IMG_PAIR_5_2 = IMAGES_PATH_ROOT + '/pair5_2.jpeg'


class MemoryGame:
    def __init__(self):
        self.shapes_arrangement = []

        self.rectangles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

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

        self.RectangleObjects = (
            Rectangle1, Rectangle2, Rectangle3, Rectangle4, Rectangle5, Rectangle6, Rectangle7, Rectangle8, Rectangle9,
            Rectangle10,
            Rectangle11, Rectangle12)


    def draw_background(self):
        for i in range(12):
            pygame.draw.rect(Window, (51, 204, 204), self.RectangleObjects[i], 10)

    def start_game(self):
        for i in range(12):
            if i == 0:
                image = pygame.image.load(IMG_PAIR_0_1)
            elif i == 1:
                image = pygame.image.load(IMG_PAIR_0_2)
            elif i == 2:
                image = pygame.image.load(IMG_PAIR_1_1)
            elif i == 3:
                image = pygame.image.load(IMG_PAIR_1_2)
            elif i == 4:
                image = pygame.image.load(IMG_PAIR_2_1)
            elif i == 5:
                image = pygame.image.load(IMG_PAIR_2_2)
            elif i == 6:
                image = pygame.image.load(IMG_PAIR_3_1)
            elif i == 7:
                image = pygame.image.load(IMG_PAIR_3_2)
            elif i == 8:
                image = pygame.image.load(IMG_PAIR_4_1)
            elif i == 9:
                image = pygame.image.load(IMG_PAIR_4_2)
            elif i == 10:
                image = pygame.image.load(IMG_PAIR_5_1)
            elif i == 11:
                image = pygame.image.load(IMG_PAIR_5_2)
            x = random.choice(self.rectangles)
            self.shapes_arrangement.append(x)
            draw_image(x, image)
            self.rectangles.remove(x)


    def shape_index(self, mouse_position):
        for i in range(12):
            if self.RectangleObjects[i].collidepoint(mouse_position):
                return self.shapes_arrangement.index(i + 1)


    def rec_number(self, mouse_position):
        for i in range(12):
            if self.RectangleObjects[i].collidepoint(mouse_position):
                return i + 1

    def hide(self, mouse_position):
        rectangle_number = self.rec_number(mouse_position)
        for i in range(12):
            if rectangle_number == i + 1:
                pygame.draw.rect(Window, (255, 255, 255), self.RectangleObjects[i].inflate(-10, -10))


    def right_choice(self, first_choice, second_choice):
        x = self.shape_index(first_choice)
        y = self.shape_index(second_choice)
        if (x == 0 and y == 1 or x == 1 and y == 0) \
                or (x == 2 and y == 3 or x == 3 and y == 2) \
                or (x == 4 and y == 5 or x == 5 and y == 4) \
                or (x == 6 and y == 7 or x == 7 and y == 6) \
                or (x == 8 and y == 9 or x == 9 and y == 8) \
                or (x == 10 and y == 11 or x == 11 and y == 10):
            return True

    def show(self, mouse_position):
        rectangle_number = self.rec_number(mouse_position)
        pressed_shape_index = self.shape_index(mouse_position)

        if pressed_shape_index == 0:
            image = pygame.image.load(IMG_PAIR_0_1)
        elif pressed_shape_index == 1:
            image = pygame.image.load(IMG_PAIR_0_2)
        elif pressed_shape_index == 2:
            image = pygame.image.load(IMG_PAIR_1_1)
        elif pressed_shape_index == 3:
            image = pygame.image.load(IMG_PAIR_1_2)
        elif pressed_shape_index == 4:
            image = pygame.image.load(IMG_PAIR_2_1)
        elif pressed_shape_index == 5:
            image = pygame.image.load(IMG_PAIR_2_2)
        elif pressed_shape_index == 6:
            image = pygame.image.load(IMG_PAIR_3_1)
        elif pressed_shape_index == 7:
            image = pygame.image.load(IMG_PAIR_3_2)
        elif pressed_shape_index == 8:
            image = pygame.image.load(IMG_PAIR_4_1)
        elif pressed_shape_index == 9:
            image = pygame.image.load(IMG_PAIR_4_2)
        elif pressed_shape_index == 10:
            image = pygame.image.load(IMG_PAIR_5_1)
        elif pressed_shape_index == 11:
            image = pygame.image.load(IMG_PAIR_5_2)

        draw_image(rectangle_number, image)


    def run_game(self):
        pygame.init()
        global Window
        Window = pygame.display.set_mode((410, 310))
        Window.fill((255, 255, 255))
        pygame.display.set_caption('Memory Game')

        self.draw_background()
        self.start_game()

        pygame.display.update()
        pygame.time.wait(8000)
        Window.fill((255, 255, 255))
        self.draw_background()
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
                    self.show(mouse_position)
                    pygame.display.update()
                    if flag == 0:
                        first_choice = mouse_position
                        if self.rec_number(first_choice) in true_choices:
                            flag = 0
                        else:
                            flag = 1

                    else:
                        second_choice = mouse_position
                        if self.rec_number(second_choice) in true_choices:
                            flag = 1
                        else:
                            flag = 0
                        if not (self.rec_number(first_choice) in true_choices) and not (
                                self.rec_number(second_choice) in true_choices):
                            if self.right_choice(first_choice, second_choice):
                                true_choices.append(self.rec_number(first_choice))
                                true_choices.append(self.rec_number(second_choice))
                            else:
                                pygame.time.wait(1000)
                                self.hide(first_choice)
                                self.hide(second_choice)
                                pygame.display.update()

            if len(true_choices) == 12:
                image = pygame.image.load('task5.png')
                Window.blit(image, (0, 0))
                pygame.display.update()


def draw_image(x, image):
    if x == 1:
        Window.blit(image, (5, 5))
    elif x == 2:
        Window.blit(image, (105, 5))
    elif x == 3:
        Window.blit(image, (205, 5))
    elif x == 4:
        Window.blit(image, (305, 5))
    elif x == 5:
        Window.blit(image, (5, 105))
    elif x == 6:
        Window.blit(image, (105, 105))
    elif x == 7:
        Window.blit(image, (205, 105))
    elif x == 8:
        Window.blit(image, (305, 105))
    elif x == 9:
        Window.blit(image, (5, 205))
    elif x == 10:
        Window.blit(image, (105, 205))
    elif x == 11:
        Window.blit(image, (205, 205))
    elif x == 12:
        Window.blit(image, (305, 205))