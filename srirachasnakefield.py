import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()

size = width, height = 800, 600
sky_color = 0, 200, 0
fps = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sriracha Snake Field')


snake_img1 = pygame.image.load("snake1.png").convert_alpha()
snake_img11 = pygame.image.load("snake1-1.png").convert_alpha()
snake_img2 = pygame.image.load("snake2.png").convert_alpha()
snake_img22 = pygame.image.load("snake2-1.png").convert_alpha()
grass_img1 = pygame.image.load("grass1.png").convert_alpha()
grass_img2 = pygame.image.load("grass2.png").convert_alpha()
bottle_img = pygame.image.load("bottle.png").convert_alpha()

snake_r = snake_img1
snake_l = snake_img2

class Snake:
    def __init__(self):
        self.x = randint(-300,800)
        self.direction = randint(0,1)
        self.speed = 5
        if self.direction == 1:
            self.speed = -5
    def move(self):
        self.x += self.speed
        if self.x > 800:
            self.x = -300
        if self.x < -300:
            self.x = 800

    def get_x(self):
        self.move()
        return self.x

    def get_direction(self):
        return self.direction

snake_list = []

for x in range(0, 13):
    snake_list.append(Snake())

scroll_y = 0
bottle_x = 425
while True:
    clock.tick(fps)

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]: bottle_x -= 5
    if keys[K_RIGHT]: bottle_x += 5
    if keys[K_ESCAPE]: sys.exit()

    if bottle_x < 0: bottle_x = 0
    elif bottle_x > 750: bottle_x = 750

    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()

    screen.fill(sky_color)

    for y in range(0,13):

        if snake_list[y].get_direction() == 1:
            screen.blit(snake_l,(snake_list[y].get_x(),y * 50 + 10))
        else:
            screen.blit(snake_r,(snake_list[y].get_x(),y * 50 + 10))
        if y % 2 == 0:
            screen.blit(grass_img1,(0,y * 50 + scroll_y - 50))
        else:
            screen.blit(grass_img2,(0,y * 50 + scroll_y - 50))
    scroll_y += 5
    if scroll_y == 50:
        scroll_y = 0

    screen.blit(bottle_img,(bottle_x,525))
    pygame.display.flip()
