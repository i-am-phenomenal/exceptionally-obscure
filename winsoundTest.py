# import winsound
# import time
# from threading import Thread
# from playsound import playsound
#
# def play_music():
#     playsound("C:/practice Programs/MarioTheme.mp3.mp3", winsound.SND_ALIAS)
#
# while True:
#     thread = Thread(target = play_music)
#     thread.start()
#     print("Testing")
#     time.sleep(1)


# import turtle
#
# turtle = turtle.Turtle()
# turtle.home()
# turtle.begin_poly()

# import pygame
# import random
#
# white_color = (255, 255, 255)
#
#
# class Block(pygame.sprite.Sprite):
#     def __init__(self, color, width, height):
#         super().__init__()
#         self.image = pygame.Surface([width, height])
#         self.image.fill(white_color)
#         # self.image.set_colorkey(self.image, color, [0, 0, width, height])
#         self.image.set_colorkey(white_color)
#         self.rect = self.image.get_rect()
#
#
# block_object = Block(white_color, 100, 20)
#
# pygame.init()
# window = pygame.display.set_mode([700, 400])
# block_list = pygame.sprite.Group()
# all_sprites_list = pygame.sprite.Group()


# import pygame as py
#
# # define constants
# WIDTH = 500
# HEIGHT = 500
# FPS = 30
#
# # define colors
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
#
# # initialize pygame and create screen
# py.init()
# screen = py.display.set_mode((WIDTH, HEIGHT))
# # for setting FPS
# clock = py.time.Clock()
#
# rot = 0
# rot_speed = 2
#
# # define a surface (RECTANGLE)
# image_orig = py.Surface((100, 100))
# # for making transparent background while rotating an image
# image_orig.set_colorkey(BLACK)
# # fill the rectangle / surface with green color
# image_orig.fill(GREEN)
# # creating a copy of orignal image for smooth rotation
# image = image_orig.copy()
# image.set_colorkey(BLACK)
# # define rect for placing the rectangle at the desired position
# rect = image.get_rect()
# rect.center = (WIDTH // 2, HEIGHT // 2)
# # keep rotating the rectangle until running is set to False
# running = True
# while running:
#     # set FPS
#     clock.tick(FPS)
#     # clear the screen every time before drawing new objects
#     screen.fill(BLACK)
#     # check for the exit
#     for event in py.event.get():
#         if event.type == py.QUIT:
#             running = False
#
#     # making a copy of the old center of the rectangle
#     old_center = rect.center
#     # defining angle of the rotation
#     rot = (rot + rot_speed) % 360
#     # rotating the orignal image
#     new_image = py.transform.rotate(image_orig, rot)
#     rect = new_image.get_rect()
#     # set the rotated rectangle to the old center
#     rect.center = old_center
#     # drawing the rotated rectangle to the screen
#     screen.blit(new_image, rect)
#     # flipping the display after drawing everything
#     py.display.flip()
#
# py.quit()


import sys, os, pygame
from math import sin, cos, pi, radians
from pygame.locals import *

# from standard_object_creator import *

screenH = 700
screenW = 800
clock =

center_of_rotation_x = screenW / 2
center_of_rotation_y = screenH / 2
radius = 200
angle = radians(45)
omega = 0.1

window = pygame.display.set_mode((screenW, screenH))
shouldExitGame = True

pygame.init()


def rotate_object():
    global angle, center_of_rotation_x, center_of_rotation_y, omega, radius
    x = center_of_rotation_x + radius * cos(angle)
    y = center_of_rotation_y - radius * sin(angle)
    rectangle = pygame.draw.rect(window, (238, 154, 73), pygame.Rect(430, 170, 10, 50))
    rect_surface = pygame.Surface((rectangle.w, rectangle.h))
    window.blit(rect_surface, (x, y))
    angle = angle + omega
    x = x + radius * omega * cos(angle + (pi / 2))
    y = y - radius * omega * sin(angle + (pi / 2))


while shouldExitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shouldExitGame = False

    pressedKey = pygame.key.get_pressed()
    if pressedKey[pygame.K_UP]:
        rotate_object()

    pygame.display.flip()
